# Title: Car Data
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: Contains all information necessary for display. Any variable that is received via CAN should be stored in this script.

from enum import Enum

class DriveState(Enum):                             # Drive State Type Enumerable
    INITIALIZING = 0,                               # Initialization State of ECU
    LV_DRIVEOFF  = 1,                               # Low-Voltage State
    HV_DRIVEOFF  = 2,                               # High-Voltage State
    HV_DRIVEON   = 3                                # Ready-to-Drive State

class InputTypes(Enum):
    BUTTON_WHEEL_LEFT  = 0,                         # Left Button of Steering Wheel
    BUTTON_WHEEL_RIGHT = 1,                         # Right Button of Steering Wheel
    BUTTON_DASH_LEFT   = 2,                         # Left Button of Dashboard
    BUTTON_DASH_RIGHT  = 3                          # Right Button of Dashboard

# Pedal Info
apps1         = 0                                   # Real APPS-1 Value from ACAN
apps2Raw      = 0                                   # Real APPS-2 Value from ACAN
brake1        = 0                                   # Real Brake-1 Value from ACAN
brake2        = 0                                   # Real Brake-2 Value from ACAN

apps1Percent  = 0                                   # APPS-1 Percentage from ECU
apps2Percent  = 0                                   # APPS-2 Percentage from ECU
brake1Percent = 0                                   # Brake-1 Percentage from ECU
brake2Percent = 0                                   # Brake-2 Percentage from ECU

apps1Max      = 0                                   # APPS-1 Calibration Maximum from Memory
apps2RawMax   = 0                                   # APPS-2 Calibration Maximum from Memory
apps1Min      = 0                                   # APPS-1 Calibration Minimum from Memory
apps2RawMin   = 0                                   # APPS-2 Calibration Minimum from Memory

accelerating  = False                               # Acceleration State from ECU
braking       = False                               # Braking State from ECU

# Vehicle States
driveState      = DriveState.INITIALIZING           # Current Drive State from ECU
driveStatePrime = DriveState.INITIALIZING           # Prior Drive State from ECU
drsState        = False                             # Current DRS State from ECU 
regenState      = False                             # Current Regen Braking State from ECU

# Acumulator Info
stateOfCharge         = 0                           # State of Charge from BMS

# Inverter Temperature
temp1                 = 0
temp2                 = 0
temp3                 = 0

# Motor Info
rpm                   = 0                           # Current RPM from the Inverter
rpmPercent            = 0                           # Current RPM as a Percentage
speedMph              = 0                           # Current Speed from the Inverter

# Errors
error25_5Implasible   = False                       # 25/5 APPS Implausibility from ECU
errorInverterFault    = False                       # Inverter Fault detected from ECU
errorAcanImplausible  = False                       # ACAN Value Implausibility from ECU
error100MsImplausible = False                       # 100ms Implausibility from ECU

# Torque
torquePercentageMax   = 0                           # Maximum Torque Percentage from ECU
torquePercentageRegen = 0                           # Maximum Regen Percentage from ECU

# Miscellaneous
lvBatteryVoltage = 0                                # Voltage of the LV Battery from ECU