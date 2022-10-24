# Title: Car Data
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: Contains all information necessary for display. Any variable that is received via CAN should be stored in this script.
# To Do: Implement CAN backend and use default values fitting safety guidelines

from enum import Enum

# Pedal Info
apps1     = 200                                     # Real APPS-1 Value from ACAN
apps2Raw  = 0                                       # Real APPS-2 Value from ACAN
brake1    = 300                                     # Real Brake-1 Value from ACAN
brake2    = 0                                       # Real Brake-2 Value from ACAN

apps1Percent  = 0.1                                 # APPS-1 Percentage from ECU
apps2Percent  = 0                                   # APPS-2 Percentage from ECU
brake1Percent = 0.79                                # Brake-1 Percentage from ECU
brake2Percent = 0                                   # Brake-2 Percentage from ECU

accelerating = False                                # Acceleration State from ECU
braking      = False                                # Braking State from ECU

apps1Max     = 500                                  # APPS-1 Calibration Maximum from Memory
apps2RawMax  = 700                                  # APPS-2 Calibration Maximum from Memory
apps1Min     = 50                                   # APPS-1 Calibration Minimum from Memory
apps2RawMin  = 70                                   # APPS-2 Calibration Minimum from Memory
brake1Max    = 400                                  # Brake-1 Calibration Maximum from Memory
brake2Max    = 400                                  # Brake-2 Calibration Maximum from Memory
brake1Min    = 90                                   # Brake-1 Calibration Minimum from Memory
brake2Min    = 90                                   # Brake-2 Calibration Minimum from Memory

# Vehicle States
class DriveState(Enum):                             # Drive State Type Enumerable
    INITIALIZING = 0,
    LV_DRIVEOFF  = 1,
    HV_DRIVEOFF  = 2,
    HV_DRIVEON   = 3
driveState = DriveState.HV_DRIVEON                  # Current Drive State from ECU
drsState     = False                                # Current DRS State from ECU 
regenState   = False                                # Current Regen Braking State from ECU

# Acumulator Info
stateOfCharge         = 86
temp1                 = 48.5
temp2                 = 102.4
temp3                 = 35.1

# Motor Info
rpmPercent            = 0.87
torquePercent         = 0.4
speed                 = 69

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