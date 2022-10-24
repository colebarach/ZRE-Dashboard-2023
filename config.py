# Title: Dashboard Configuration
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: Contains all variables related to the layout and rendering of the GUI. Anything views or widget present in the GUI should
#   be customizable through variables in this script.

# Screen Properties
SCREEN_W = 1024
SCREEN_H = 600

# GUI Style
#   Font
font                   = "ExcludedItalic"
fontSmall              = (font, 16)
fontMedium             = (font, 20)
fontLarge              = (font, 28)
fontExtraLarge         = (font, 182)
#   Colors
fontColor              = '#FFFFFF'
highlightColor         = '#FFFFFF'
lowlightColor          = '#AAAAAA'
backgroundColor        = '#000000'
colorGreen             = '#44FF44'
colorYellow            = '#FFFF44'
colorRed               = '#FF4444'
colorDarkGreen         = '#004400'
colorDarkYellow        = '#444400'
colorDarkRed           = '#440000'
colorBlue              = "#4444FF"
#   Spacing
padding                = 8
borderWidth            = 2
strataWidth            = 12
strataShear            = 30

# Driving Views
#   Side Bars
sideBarFont            = fontLarge
sideBarWidths          = 70
sideBarAppsColor       = colorGreen
sideBarBrakeColor      = colorRed
sideBarAppsLabel       = "T\nH\nR\nO\nT\nT\nL\nE"
sideBarBrakeLabel      = "B\nR\nA\nK\nE"
#   Shortcut Bar
shortcutBarFont        = fontSmall
shortcutBarHeight      = 80
#   Display Number
displayNumberStatFont  = fontExtraLarge
displayNumberLabelFont = fontLarge
displayNumberWidth     = 340
displayNumberHeight    = 220
displayNumberSpeedText = "MPH"
#   Info Panel
infoPanelStatFont      = fontLarge
infoPanelLabelFont     = fontMedium
infoPanelWidth         = 220
infoPanelHeight        = 150
infoPanelStatWidth     = 100
infoPanelSidePadding   = 10
#   RPM Bar
rpmBarHeight           = 80
rpmBarLabelHeight      = 22
rpmBarFont             = fontSmall
rpmHighColors          = [colorGreen,     colorYellow,     colorRed]
rpmLowColors           = [colorDarkGreen, colorDarkYellow, colorDarkRed]
rpmRanges              = [0.65, 0.78, 1]
rpmLabelValues         = ["2500", "5000", "7500", "10000", "12500"]
#   Torque Bar
torqueBarWidth         = 800
torqueBarHeight        = 8
torqueBarLabelHeight   = 22
torqueBarText          = "Torque"
torqueBarTextFont      = fontSmall
torqueBarColor         = colorBlue

# Statistics
#   Temperature
temperatureRanges      = [40, 50, 60]
temperatureRangeColors = [colorGreen, colorYellow, colorRed]
def GetTemperatureColor(temperature):
    for index in range(len(temperatureRanges)):
        if(temperature < temperatureRanges[index]):
            return temperatureRangeColors[index]
    return temperatureRangeColors[len(temperatureRangeColors)-1]