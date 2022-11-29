# Title: Car Data
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.11.19
# Function: Contains all information necessary for display. Any variable that is received via CAN should be stored in this script.

from enum import Enum

# Input ---------------------------------------------------------------------------------------------------
class InputTypes(Enum):                              # Input Type Enumerable
    BUTTON_WHEEL_LEFT  = 0,                          # - Left Button of Steering Wheel
    BUTTON_WHEEL_RIGHT = 1,                          # - Right Button of Steering Wheel
    BUTTON_DASH_LEFT   = 2,                          # - Left Button of Dashboard
    BUTTON_DASH_RIGHT  = 3                           # - Right Button of Dashboard

# Communications ------------------------------------------------------------------------------------------
acanCanActive          = False                       # Activity of the ACAN CAN
ecuCanActive           = False                       # Activity of the ECU CAN
bmsCanActive           = False                       # Activity of the BMS CAN
inverterCanActive      = False                       # Activity of the Inverter CAN

# Pedal Info ----------------------------------------------------------------------------------------------
apps1                  = None                        # Real APPS-1 Value from ACAN
apps2Raw               = None                        # Real APPS-2 Value from ACAN
brake1                 = None                        # Real Brake-1 Value from ACAN
brake2                 = None                        # Real Brake-2 Value from ACAN

apps1Percent           = None                        # APPS-1 Percentage from ECU
apps2Percent           = None                        # APPS-2 Percentage from ECU
brake1Percent          = None                        # Brake-1 Percentage from ECU
brake2Percent          = None                        # Brake-2 Percentage from ECU

apps1Max               = None                        # APPS-1 Calibration Maximum
apps2RawMax            = None                        # APPS-2 Calibration Maximum
apps1Min               = None                        # APPS-1 Calibration Minimum
apps2RawMin            = None                        # APPS-2 Calibration Minimum

accelerating           = None                        # Acceleration State (True => Accelerating)
braking                = None                        # Braking State (True => Braking)

# ECU Info ------------------------------------------------------------------------------------------------
class DriveState(Enum):                              # Drive State Type Enumerable
    INITIALIZING       = 0,                          # - Initialization State of ECU
    LV_DRIVEOFF        = 1,                          # - Low-Voltage State
    HV_DRIVEOFF        = 2,                          # - High-Voltage State
    HV_DRIVEON         = 3                           # - Ready-to-Drive State

driveState             = DriveState.INITIALIZING     # Current Drive State of the Vehicle
driveStatePrime        = None                        # Prior Drive State of the Vehicle
drsState               = None                        # Current DRS State of the Vehicle
regenState             = None                        # Current Regen Braking State of the Vehicle
lvBatteryVoltage       = None                        # Voltage of the LV Battery

# Acumulator Data -----------------------------------------------------------------------------------------
stateOfCharge          = None                        # State of Charge
packCurrent            = None                        # Current of the Accumulator
cellVoltages           = [None]*90                   # Accumulator Cell Voltages
cellBalancings         = [None]*90                   # Accumulator Cell Balancings
cellVoltageMax         = None                        # Accumulator Highest Cell Voltage
cellVoltageMin         = None                        # Accumulator Lowest Cell Voltage
packTemperatures       = [None]*45                   # Accumulator Pack Temperatures
packTemperatureMax     = None                        # Highest Pack Temperature
packTemperatureMean    = None
segmentSenseLines      = [None]*5                    # Accumulator Segment Sense Line Statuses

# Inverter Data -------------------------------------------------------------------------------------------
inverterTempGdb        = None                        # Temperature of the Inverter GBD
inverterTempModuleA    = None                        # Temperature of the Inverter Module A
inverterTempModuleB    = None                        # Temperature of the Inverter Module B
inverterTempModuleC    = None                        # Temperature of the Inverter Module C
inverterTempCb         = None                        # Temperature of the Inverter CB
inverterTempMean       = None                        # Average Temperature of the Inverter
inverterTempMax        = None                        # Maximum Temperature of the Inverter

# Motor Data ----------------------------------------------------------------------------------------------
motorRpm               = None                        # RPM of the Motor
motorSpeedMph          = None                        # Speed of the Vehicle
torquePercentageMax    = None                        # Maximum Torque Percentage from ECU
torquePercentageRegen  = None                        # Maximum Regen Percentage from ECU
motorTemperature       = None                        # Temperature of the Motor

# Errors --------------------------------------------------------------------------------------------------
error25_5Implasible    = None                        # 25/5 APPS Implausibility
errorInverterFault     = None                        # Inverter Fault Detected
errorAcanImplausible   = None                        # ACAN Value Implausibility
error100MsImplausible  = None                        # 100ms APPS Implausibility
errorBmsTempFault      = None                        # BMS Temperature Fault
errorBmsVoltageFault   = None                        # BMS Voltage Fault
errorBmsSelfTestFault  = None                        # BMS Self Test Fault
errorBmsSenseLineFault = None                        # BMS Sense Line Fault