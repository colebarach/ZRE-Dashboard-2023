# CAN Bus -------------------------------------------------------------------------------------------------
CAN_BITRATE                      = 1000000                     # CAN Bitrate of 1 Megabit per Second
CAN_ID_INPUT_PEDALS              = 0x005                       # ID of Input_Pedals
CAN_ID_DATA_TEMP_1               = 0x0A0                       # ID of Data_Temperature_1
CAN_ID_DATA_TEMP_2               = 0x0A1                       # ID of Data_Temperature_2
CAN_ID_DATA_TEMP_3               = 0x0A2                       # ID of Data_Temperature_3_Torque
CAN_ID_DATA_MOTOR                = 0x0A5                       # ID of Data_Motor
CAN_ID_CELL_VOLTAGES_START       = 0x401                       # ID of Cell_Voltages_01_04
CAN_ID_CELL_VOLTAGES_END         = 0x417                       # ID of Cell_Voltages_88_89
CAN_ID_PACK_TEMPERATURES_START   = 0x41B                       # ID of Pack_Temperatures_00_03
CAN_ID_PACK_TEMPERATURES_END     = 0x426                       # ID of Pack_Temperatures_44
CAN_ID_CELL_BALANCINGS_START     = 0x418                       # ID of Cell_Balancings_00_35
CAN_ID_CELL_BALANCINGS_END       = 0x41A                       # ID of Cell_Balancings_72_89
CAN_ID_STATUS_BMS                = 0x440                       # ID of Status_BMS
CAN_ID_DATA_PEDALS               = 0x701                       # ID of Data_Pedals
CAN_ID_STATUS_ECU                = 0x703                       # ID of Status_ECU

CAN_ID_COMMAND_APPS_CALIBRATION  = 0x533                       # ID of Command_APPS_Calibration

canMessageTimeout                = 1                           # Length of Time for CAN Activity to Expire

# CAN Data Interpretation ---------------------------------------------------------------------------------
RPM_MAX                          = 5500                        # Maximum RPM Value
INVERTER_RPM_SCALE               = 1                           # Inverter RPM Scale Factor
INVERTER_TEMP_SCALE              = 0.1                         # Inverter Temperature Scale Factor

APPS_1_PERCENT_SCALE             = 0.1                         # APPS-1 Percent Scale Factor
APPS_2_PERCENT_SCALE             = 0.1                         # APPS-2 Percent Scale Factor
BRAKE_1_PERCENT_SCALE            = 0.1                         # Brake-1 Percent Scale Factor
BRAKE_2_PERCENT_SCALE            = 0.1                         # Brake-2 Percent Scale Factor

LV_BATTERY_VOLTAGE_SCALE         = 0.0196888                   # Low-Voltage Battery Voltage Scale FactorS
CELL_VOLTAGE_SCALE               = 0.0001                      # Cell Voltage Scale Factor
PACK_TEMPERATURE_SCALE           = -0.0021933                  # Pack Temperature Scale Factor
PACK_TEMPERATURE_OFFSET          = 81.297                      # Pack Temperature Offset Factor
STATE_OF_CHARGE_SCALE            = 0.1                         # State of Charge Scale Factor
PACK_CURRENT_LO_SCALE            = 0.01                        # Pack Current Lo Byte Scale Factor

# Mechanical Data - 2022 ----------------------------------------------------------------------------------
RADIANS_PER_ROTATION             = 6.283185307                 # Number of Radians per Rotation (2 * PI)
TIRE_RADIUS_INCHES               = 9                           # Radius of the Vehicle Rear Tire
SPROCKET_TEETH_COUNT             = 40                          # Number of Teeth on Axle Sprocket
MOTOR_TEETH_COUNT                = 13                          # Number of Teeth on Motor Sprocket
MINUTES_PER_HOUR                 = 60                          # Number of Minutes per Hour
INCHES_PER_FOOT                  = 12                          # Number of Inches per Foot
FEET_PER_MILE                    = 5280                        # Number of Feet per Mile