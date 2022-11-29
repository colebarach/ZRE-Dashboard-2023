# Title: Dashboard Configuration
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.11.25
# Function: Contains all variables related to the layout and rendering of the GUI. Anything views or widget present in the GUI should
#   be customizable through variables in this script.

# Screen Properties ---------------------------------------------------------------------------------------
SCREEN_W = 1024                                                # Pixel Width of the GUI
SCREEN_H = 600                                                 # Pixel Height of the GUI

# CAN Bus -------------------------------------------------------------------------------------------------
CAN_BITRATE                      = 1000000                     # CAN Bitrate of 1 Megabit per Second
CAN_ID_INPUT_PEDALS              = 0x005                       # ID of Input_Pedals
CAN_ID_DATA_MOTOR                = 0x0A5                       # ID of Data_Motor
CAN_ID_DATA_PEDALS               = 0x701                       # ID of Data_Pedals
CAN_ID_STATUS_ECU                = 0x703                       # ID of Status_ECU

CAN_ID_COMMAND_APPS_CALIBRATION  = 0x533                       # ID of Command_APPS_Calibration

CAN_ID_CELL_VOLTAGES_START       = 0x401                       # ID of Cell_Voltages_01_04
CAN_ID_CELL_VOLTAGES_END         = 0x417                       # Number of Sequential Cell Voltage IDs

canMessageTimeout                = 0.5                         # Length of Time for CAN Activity to Expire
emulateCan                       = True                        # Use Real CAN Data or Emulation

# CAN Data Interpretation ---------------------------------------------------------------------------------
RPM_MAX                          = 5500                        # Maximum RPM Value
LV_BATTERY_VOLTAGE_SCALE         = 0.0196888                   # Low-Voltage Battery Voltage Scale Factor

APPS_1_PERCENT_SCALE             = 0.1                         # APPS-1 Percent Scale Factor
APPS_2_PERCENT_SCALE             = 0.1                         # APPS-2 Percent Scale Factor
BRAKE_1_PERCENT_SCALE            = 0.1                         # Brake-1 Percent Scale Factor
BRAKE_2_PERCENT_SCALE            = 0.1                         # Brake-2 Percent Scale Factor

# Mechanical Data - 2022 ----------------------------------------------------------------------------------
RADIANS_PER_ROTATION             = 6.283185307                 # Number of Radians per Rotation (2 * PI)
TIRE_RADIUS_INCHES               = 9                           # Radius of the Vehicle Rear Tire
SPROCKET_TEETH_COUNT             = 40                          # Number of Teeth on Axle Sprocket
MOTOR_TEETH_COUNT                = 13                          # Number of Teeth on Motor Sprocket
MINUTES_PER_HOUR                 = 60                          # Number of Minutes per Hour
INCHES_PER_FOOT                  = 12                          # Number of Inches per Foot
FEET_PER_MILE                    = 5280                        # Number of Feet per Mile

# Dashboard Theme -----------------------------------------------------------------------------------------
# Font
dashFont                       = "ExcludedItalic"              # Main Font
dashFontBare                   = "Consolas Bold"               # Bare Font
dashFontExtraSmall             = (dashFont, 10)                # Extra Small Font Size
dashFontSmall                  = (dashFont, 18)                # Small Font Size
dashFontMedium                 = (dashFont, 20)                # Medium Font Size
dashFontLarge                  = (dashFont, 28)                # Large Font Size
dashFontExtraLarge             = (dashFont, 182)               # Extra Large Font Size
dashFontBareSmall              = (dashFontBare, 12)            # Small Bare Font Size
# Colors
dashFontColor                  = '#FFFFFF'                     # Main Font Color
dashHighlight                  = '#FFFFFF'                     # Main Highlight Color
dashLowlight                   = '#AAAAAA'                     # Main Lowlight Color
dashBackground                 = '#000000'                     # Main Background Color
dashGreen                      = '#44FF44'                     # Green Palette
dashYellow                     = '#FFFF44'                     # Yellow Palette
dashRed                        = '#FF4444'                     # Red Palette
dashBlue                       = "#4444FF"                     # Blue Palette
dashDarkGreen                  = '#004400'                     # Dark Green Palette
dashDarkYellow                 = '#444400'                     # Dark Yellow Palette
dashDarkRed                    = '#440000'                     # Dark Red Palette
dashGrey                       = '#444444'                     # Grey Palette
# Spacing
dashPadding                    = 8                             # Main Padding
dashBorderWidth                = 2                             # Main Border Pixel Width
dashBorderLight                = 1                             # Main Light Border Pixel Width
# Strata Bar
dashStrataSize                 = 12                            # Main Strata-Bar Pixel Size
dashStrataGap                  = 12                            # Main Strata-Bar Pixel Gap Size
dashStrataSlope                = 0.5                           # Main Strata-Bar Slope

# Debug Theme ---------------------------------------------------------------------------------------------
# Font
plainFont                      = 'Consolas'                    # Dafault Font
plainFontSmall                 = (plainFont, 8)                # Small Default Font
plainFontMedium                = (plainFont, 10)               # Medium Default Font
# Colors
plainFontColor                 = '#000000'                     # Default Font Color
plainBackground                = '#F0F0F0'                     # Default Background Color
plainHighlight                 = '#AAAAAA'                     # Default Highlight Color
plainLowlight                  = '#444444'                     # Default Lowlight Color
plainBlue                      = '#023399'                     # Default Blue Palette 
# Spacing
plainPadding                   = 4                             # Default Padding
plainBorderWidth               = 1                             # Default Border Width
# Strata Bar
plainStrataSize                = 8                             # Default Strata-Bar Size
plainStrataGap                 = 2                             # Default Strata-Bar Gap
plainStrataSlope               = 0                             # Default Strata-Bar Slope

# Low Voltage View ----------------------------------------------------------------------------------------
lvFontSize                     = dashFontLarge                 # Low-Voltage Font Size

# Drive View ----------------------------------------------------------------------------------------------
# Side Bars
driveSideBarFont               = dashFontLarge                 # Side Bars Label Fonts
driveSideBarWidth              = 70                            # Side Bar Pixel Width
# Button Bar
driveButtonBarFont             = dashFontSmall                 # Button Bar Label Font
driveButtonBarHeight           = 80                            # Button Bar Pixel Height
# Side Panels
driveSidePanelStatFont         = dashFontLarge                 # Side Panel Statistic Font
driveSidePanelLabelFont        = dashFontMedium                # Side Panel Label Font
driveSidePanelWidth            = 220                           # Side Panel Pixel Width
driveSidePanelHeight           = 180                           # Side Panel Pixel Height
driveSidePanelStatHeight       = 40                            # Side Panel Statistic Pixel Height
# Center Panels
driveCenterPanelStatFont       = dashFontExtraLarge            # Center Panel Statistic Font
driveCenterPanelLabelFont      = dashFontLarge                 # Center Panel Label Font
driveCenterPanelStatWidth      = 340                           # Center Panel Statistic Pixel Width
driveCenterPanelStatHeight     = 140                           # Center Panel Statistic Pixel Height
# Top Bar
driveTopBarHeight              = 100                           # Top Bar Pixel Height
# Bottom Bars
driveBottomBarLabelFont        = dashFontExtraSmall            # Bottom Bar Label Font
driveBottomBarHeight           = 8                             # Bottom Bar Pixel Height
driveBottomBarLabelWidth       = 16                            # Bottom Bar Label Pixel Width
driveBottomBarLabelHeight      = 9                             # Bottom Bar Label Pixel Height

# BMS View ------------------------------------------------------------------------------------------------
# Stat Panel
bmsStatPanelHeight             = 200                           # Stat Panel Pixel Height
bmsFaultCodeWidth              = 260                           # Fault Column Pixel Width
# Voltage Panel
bmsCellPanelWidth              = 900                           # Voltage Panel Pixel Width
bmsCellPanelHeight             = 250                           # Voltage Panel Pixel Height
# Button Panel
bmsButtonPanelHeight           = 90                            # Button Panel Pixel Height

# Statistics ----------------------------------------------------------------------------------------------
# Pedals
brakeColor                     = dashRed                       # Color of Brake Bar
appsColor                      = dashGreen                     # Color of APPS Bar
torqueColor                    = dashBlue                      # Color of Torque Bar
regenColor                     = dashGreen                     # Color of Regen Bar

# RPM
rpmHighlight                   = [dashGreen, dashYellow, dashRed]
rpmLowlight                    = [dashDarkGreen, dashDarkYellow, dashDarkRed]
rpmDomain                      = [3000, 4500, 5500]

# Temperature
tempHighlight                  = [dashGreen, dashYellow, dashRed]
tempPalette                    = ['#66FF66', '#DDDD66', '#FF6666']
tempDomain                     = [30, 50, 60]

# Voltage
balancingPalette               = [dashGrey, '#22BBBB', '#22BB22']
voltageErrorColor              = dashRed
voltageRange                   = (2.7, 4.2)

# Debug Menu ----------------------------------------------------------------------------------------------
debugGuiWidth                  = 600