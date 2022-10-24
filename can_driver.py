# Title: Main CAN Script
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: The main script for CAN communications. Responsible for handling all messages from the CAN receivers and 

import car_data

# Message 0x005 - Pedal Data from ACAN
def handleInputPedals(data):
    # Bytes 0 & 1
    car_data.apps1    = data[0] | (data[1] << 8)
    # Bytes 2 & 3
    car_data.apps2Raw = data[2] | (data[3] << 8)
    # Bytes 4 & 5
    car_data.brake1   = data[4] | (data[5] << 8)
    # Bytes 6 & 7
    car_data.brake2   = data[6] | (data[7] << 8)

# Message 0x701 - Pedal Data from ECU
def handleDataPedals(data):
    # Byte 0
    car_data.apps1Percent  = data[0]
    # Byte 1
    car_data.apps2Percent  = data[1]
    # Byte 2
    car_data.brake1Percent = data[2]
    # Byte 3
    car_data.brake2Percent = data[3]

# Message 0x703 - Status Message from ECU
def handleStatusEcu(data):
    # Byte 0
    car_data.driveState            = data[0] & 0b00000011
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
    lvBatteryVoltageRaw = data[4] | (data[5] << 8)
    car_data.lvBatteryVoltage = lvBatteryVoltageRaw * 0.0196888
    # Bytes 6 & 7
    # Ignore, data is invalid