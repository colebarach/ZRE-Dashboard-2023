# Title: Main CAN Script
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: The main script for CAN communications. Responsible for handling all messages from the CAN receivers and 

# Libraries
import os
import sys

# Includes
import car_data
import can_windows
import gui
import config

online = True

def Begin():
    Initialize()
    Update()

def Initialize():
    global canMaster
    print("CAN - Initializing...")
    if(sys.platform == 'win32'): canMaster = can_windows
    canMaster.Initialize()

def Update():
    global canMaster
    global online
    print("CAN - Loop Starting...")
    while(online):
        canMaster.Update()
    print("CAN - Loop Ended")
    canMaster.Close()

def Close():
    global online
    online = False
    print("CAN - Closing...")

# Message Handling ----------------------------------------------------------------------------------------

# Message 0x005 - Pedal Data from ACAN
def HandleInputPedals(data):
    # Bytes 0 & 1
    car_data.apps1    = data[0] | (data[1] << 8)
    # Bytes 2 & 3
    car_data.apps2Raw = data[2] | (data[3] << 8)
    # Bytes 4 & 5
    car_data.brake1   = data[4] | (data[5] << 8)
    # Bytes 6 & 7
    car_data.brake2   = data[6] | (data[7] << 8)

def HandleDataMotor(data):
    car_data.rpm = InterpretSignedNBitInt(data[2] | (data[3] << 8))
    car_data.rpmPercent =       abs(100 * car_data.rpm / config.RPM_MAX)
    car_data.speedMph   = round(abs(car_data.rpm * config.RPM_TO_MPH_SCALE))

# Message 0x701 - Pedal Data from ECU
def HandleDataPedals(data):
    # Byte 0
    car_data.apps1Percent  = (data[0] | (data[1] << 8)) * config.APPS_1_PERCENT_SCALE
    # Byte 1
    car_data.apps2Percent  = (data[2] | (data[3] << 8)) * config.APPS_2_PERCENT_SCALE
    # Byte 2
    car_data.brake1Percent = (data[4] | (data[5] << 8)) * config.BRAKE_1_PERCENT_SCALE
    # Byte 3
    car_data.brake2Percent = (data[6] | (data[7] << 8)) * config.BRAKE_2_PERCENT_SCALE

# Message 0x703 - Status Message from ECU
def HandleStatusEcu(data):
    # Byte 0
    driveState = data[0] & 0b00000011
    if(driveState == 0): car_data.driveState = car_data.DriveState.INITIALIZING
    if(driveState == 1): car_data.driveState = car_data.DriveState.LV_DRIVEOFF
    if(driveState == 2): car_data.driveState = car_data.DriveState.HV_DRIVEOFF
    if(driveState == 3): car_data.driveState = car_data.DriveState.HV_DRIVEON
    car_data.accelerating          = data[0] & 0b00000100
    car_data.braking               = data[0] & 0b00001000
    car_data.drsState              = data[0] & 0b00010000
    car_data.regenState            = data[0] & 0b00100000
    # Byte 1
    car_data.error25_5Implasible   = data[1] & 0b00000001
    car_data.errorInverterFault    = data[1] & 0b00000010
    car_data.errorAcanImplausible  = data[1] & 0b00000100
    car_data.error100MsImplausible = data[1] & 0b00001000
    # Byte 2
    car_data.torquePercentageMax   = data[2]
    # Byte 3
    car_data.torquePercentageRegen = data[3]
    # Bytes 4 & 5
    car_data.lvBatteryVoltage = (data[4] | (data[5] << 8)) * config.LV_BATTERY_VOLTAGE_SCALE
    # Bytes 6 & 7
    #   Ignore, data is invalid
    # GUI Updates
    gui.UpdateDriveState()


# Message Transmitting ------------------------------------------------------------------------------------

# Message 0x533
def SendCommandAppsCalibration():
    SendCommandAppsCalibration(car_data.apps1Min, car_data.apps1Max, car_data.apps2RawMin, car_data.apps2RawMax)
def SendCommandAppsCalibration(apps1MinValue, apps1MaxValue, apps2MinValue, apps2MaxValue):
    message = [0,0,0,0,0,0,0,0]
    message[0] = (apps1MinValue)      & 0xFF
    message[1] = (apps1MinValue >> 8) & 0xFF
    message[2] = (apps1MaxValue)      & 0xFF
    message[3] = (apps1MaxValue >> 8) & 0xFF
    message[4] = (apps2MinValue)      & 0xFF
    message[5] = (apps2MinValue >> 8) & 0xFF
    message[6] = (apps2MaxValue)      & 0xFF
    message[7] = (apps2MaxValue >> 8) & 0xFF
    canMaster.Send(config.CAN_ID_COMMAND_APPS_CALIBRATION, message)

def SendInputPedals(apps1, apps2, brake1, brake2):
    message = [0,0,0,0,0,0,0,0]
    message[0] = (apps1)       & 0xFF
    message[1] = (apps1 >> 8)  & 0xFF
    message[2] = (apps2)       & 0xFF
    message[3] = (apps2 >> 8)  & 0xFF
    message[4] = (brake1)      & 0xFF
    message[5] = (brake1 >> 8) & 0xFF
    message[6] = (brake2)      & 0xFF
    message[7] = (brake2 >> 8) & 0xFF
    canMaster.Send(config.CAN_ID_INPUT_PEDALS, message)

def SendDataMotor(motorAngle, motorRpm, motorFrequency, motorDeltaResolver):
    message = [0,0,0,0,0,0,0,0]
    message[0] =  (motorAngle * 10)           & 0xFF
    message[1] = ((motorAngle * 10) >> 8)     & 0xFF
    message[2] =  (motorRpm)                  & 0xFF
    message[3] =  (motorRpm >> 8)             & 0xFF
    message[4] =  (motorFrequency * 10)       & 0xFF
    message[5] = ((motorFrequency * 10) >> 8) & 0xFF
    message[6] =  (motorDeltaResolver)        & 0xFF
    message[7] =  (motorDeltaResolver >> 8)   & 0xFF
    canMaster.Send(config.CAN_ID_DATA_MOTOR, message)

def SendDataPedals(apps1Percent, apps2Percent, brake1Percent, brake2Percent):
    message = [0,0,0,0,0,0,0,0]
    message[0] = int(apps1Percent / config.APPS_1_PERCENT_SCALE)        & 0xFF
    message[1] = int(apps1Percent / config.APPS_1_PERCENT_SCALE) >> 8   & 0xFF
    message[2] = int(apps2Percent / config.APPS_2_PERCENT_SCALE)        & 0xFF
    message[3] = int(apps2Percent / config.APPS_2_PERCENT_SCALE) >> 8   & 0xFF
    message[4] = int(brake1Percent / config.BRAKE_1_PERCENT_SCALE)      & 0xFF
    message[5] = int(brake1Percent / config.BRAKE_1_PERCENT_SCALE) >> 8 & 0xFF
    message[6] = int(brake2Percent / config.BRAKE_2_PERCENT_SCALE)      & 0xFF
    message[7] = int(brake2Percent / config.BRAKE_2_PERCENT_SCALE) >> 8 & 0xFF
    canMaster.Send(config.CAN_ID_DATA_PEDALS, message)

def SendStatusEcu(driveStateInput, acceleratingInput, brakingInput, drsInput, regenInput, is25_5Input, inverterInput, acanInput, is100msInput, torquePercentInput, regenPercentInput, voltageLvInput, resistanceImdInput):
    message = [0,0,0,0,0,0,0,0]
    # Byte 0
    message[0] |= (driveStateInput)        & 0b00000011
    message[0] |= (acceleratingInput << 2) & 0b00000100
    message[0] |= (brakingInput      << 3) & 0b00001000
    message[0] |= (drsInput          << 4) & 0b00010000
    message[0] |= (regenInput        << 5) & 0b00100000
    # Byte 1
    message[1] |= (is25_5Input)            & 0b00000001
    message[1] |= (inverterInput     << 1) & 0b00000010
    message[1] |= (acanInput         << 2) & 0b00000100
    message[1] |= (is100msInput      << 3) & 0b00001000
    # Bytes 2 & 3
    message[2] = int(torquePercentInput) & 0xFF
    message[3] = int(regenPercentInput)  & 0xFF
    # Bytes 4 & 5
    message[4] = (int(voltageLvInput / config.LV_BATTERY_VOLTAGE_SCALE))      & 0xFF
    message[5] = (int(voltageLvInput / config.LV_BATTERY_VOLTAGE_SCALE) >> 8) & 0xFF
    # Bytes 6 & 7
    message[6] = (int(resistanceImdInput))      & 0xFF
    message[7] = (int(resistanceImdInput) >> 8) & 0xFF
    canMaster.Send(config.CAN_ID_STATUS_ECU, message)

# Data Interpretation -------------------------------------------------------------------------------------

def InterpretSignedNBitInt(value, bitCount=16):
    if(value > 2 ** (bitCount-1)): value -= 2 ** bitCount
    return value