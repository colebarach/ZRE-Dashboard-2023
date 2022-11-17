# Title: Dashboard Configuration
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: Contains all variables related to the layout and rendering of the GUI. Anything views or widget present in the GUI should
#   be customizable through variables in this script.

# Screen Properties ---------------------------------------------------------------------------------------
SCREEN_W = 1024
SCREEN_H = 600

# CAN Bus -------------------------------------------------------------------------------------------------
CAN_BITRATE = 1000000
CAN_ID_INPUT_PEDALS = 0x005
CAN_ID_DATA_MOTOR   = 0x0A5
CAN_ID_DATA_PEDALS  = 0x701
CAN_ID_STATUS_ECU   = 0x703

CAN_ID_COMMAND_APPS_CALIBRATION = 0x533

# CAN Data Interpretation ---------------------------------------------------------------------------------
RPM_MAX                  = 5000                     # Maximum RPM Value
RPM_TO_MPH_SCALE         = 0.01933745               # 2022 RPM-MPH Scale Factor
# RPM_TO_MPH_SCALE         = 0.0129818              # 2023 RPM-MPH Scale Factor
LV_BATTERY_VOLTAGE_SCALE = 0.0196888                # Low-Voltage Battery Voltage Scale Factor

APPS_1_PERCENT_SCALE    = 0.1                       # APPS-1 Percent Scale Factor
APPS_2_PERCENT_SCALE    = 0.1                       # APPS-2 Percent Scale Factor
BRAKE_1_PERCENT_SCALE   = 0.1                       # Brake-1 Percent Scale Factor
BRAKE_2_PERCENT_SCALE   = 0.1                       # Brake-2 Percent Scale Factor

# GUI Theme -----------------------------------------------------------------------------------------------
#   Font
themeFont              = "ExcludedItalic"
themeFontSmall         = (themeFont, 16)
themeFontMedium        = (themeFont, 20)
themeFontLarge         = (themeFont, 28)
themeFontExtraLarge    = (themeFont, 182)
#   Colors
themeFontColor         = '#FFFFFF'
themeHighlight         = '#FFFFFF'
themeLowlight          = '#AAAAAA'
themeBackground        = '#000000'
themeGreen             = '#44FF44'
themeYellow            = '#FFFF44'
themeRed               = '#FF4444'
themeDarkGreen         = '#004400'
themeDarkYellow        = '#444400'
themeDarkRed           = '#440000'
themeBlue              = "#4444FF"
#   Spacing
themePadding           = 8
themeBorderWidth       = 2
themeStrataSize        = 12
themeStrataGap         = 12
themeStrataSlope       = 0.8
# Debug Theme ---------------------------------------------------------------------------------------------
#   Font
plainFont              = 'Consolas'
plainFontSmall         = (plainFont, 8)
plainFontMedium        = (plainFont, 10)
#   Colors
plainFontColor         = '#000000'
plainBackground        = '#F0F0F0'
plainLowlight          = '#444444'
plainHighlight         = '#AAAAAA'
plainBlue              = '#023399'
#   Spacing
plainPadding           = 4
plainBorderWidth       = 1
#   Strata Bar
plainStrataSize        = 8
plainStrataGap         = 2
plainStrataSlope       = 0

# Driving Views -------------------------------------------------------------------------------------------
#   Side Bars
sideBarFont            = themeFontLarge
sideBarWidths          = 70
sideBarAppsColor       = themeGreen
sideBarBrakeColor      = themeRed
sideBarAppsLabel       = "THROTTLE"
sideBarBrakeLabel      = "BRAKE"
#   Shortcut Bar
# shortcutBarFont        = fontSmall
shortcutBarHeight      = 80
#   Display Number
# displayNumberStatFont  = fontExtraLarge
# displayNumberLabelFont = fontLarge
displayNumberWidth     = 340
displayNumberHeight    = 220
displayNumberSpeedText = "MPH"
#   Info Panel
# infoPanelStatFont      = fontLarge
# infoPanelLabelFont     = fontMedium
infoPanelWidth         = 220
infoPanelHeight        = 150
infoPanelStatWidth     = 100
infoPanelSidePadding   = 10
#   RPM Bar
rpmBarHeight           = 80
rpmBarLabelHeight      = 22
# rpmBarFont             = fontSmall
rpmHighlight           = [themeGreen,     themeYellow,     themeRed]
rpmLowlight            = [themeDarkGreen, themeDarkYellow, themeDarkRed]
rpmDomain              = [0.65, 0.78, 1]
# rpmLabelValues         = ["1300", "2600", "3900", "5200", "6500"]
#   Torque Bar
torqueBarWidth         = 800
torqueBarHeight        = 8
torqueBarLabelHeight   = 22
torqueBarText          = "Torque"
# torqueBarTextFont      = fontSmall
# torqueBarColor         = colorBlue

# Statistics
#   Temperature
# temperatureRanges      = [40, 50, 60]
# temperatureRangeColors = [colorGreen, colorYellow, colorRed]
# def GetTemperatureColor(temperature):
#     for index in range(len(temperatureRanges)):
#         if(temperature < temperatureRanges[index]):
#             return temperatureRangeColors[index]
#     return temperatureRangeColors[len(temperatureRangeColors)-1]

# Debug Menu ----------------------------------------------------------------------------------------------
debugGuiWidth          = 600

# def RpmToMph(rotationsPerMinute):
    # radiansPerMinute = 2*PI
    # speed = rotationsPerMinute * radiansPerRotation * tireRadiusInches * (sprocketTeethCount / motorTeethCount) * minutesPerHour / inchesPerMile