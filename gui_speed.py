# Title: GUI Speed View
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: Basic Driving View for the GUI. Displays speed and basic info.

# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

# Includes
import gui
import gui_calibration
import config
import widgets
import car_data

# Initialization
# - Creates instances of all necessary widgets
# - Should only be called once per session
def Initialize(guiRoot):
    # Root Declaration
    global root
    root = widgets.ThemeFrame(guiRoot, grid=False)

    # Root Partitioning
    displayWidth   = config.SCREEN_W - 2*config.sideBarWidths
    displayHeight  = config.SCREEN_H - config.shortcutBarHeight
    sideBarWidth   = config.sideBarWidths
    sideBarHeight  = config.SCREEN_H
    shortcutWidth  = displayWidth
    shortcutHeight = config.shortcutBarHeight
    
    root.columnconfigure(0, minsize=sideBarWidth)   # Brake Bar
    root.columnconfigure(1, minsize=displayWidth)   # Center Display
    root.columnconfigure(2, minsize=sideBarWidth)   # APPS Bar

    root.rowconfigure   (0, minsize=displayHeight)  # Center Display
    root.rowconfigure   (1, minsize=shortcutHeight) # Shortcut Bar

    # Root Widgets
    #   Shortcut Options
    shortcutCommands = [0,0,0,0]
    shortcutNames    = ["Endurance\nView", "Lap\nView", "Testing\nView", "Settings"]
    #   Widgets
    global brakeBar
    global appsBar
    brakeBar  = widgets.ThemeProgressBar(root, sideBarWidth, sideBarHeight, "Vertical", column=0, row=0, rowspan=2, border=True, text=config.sideBarBrakeLabel, foreground=config.sideBarBrakeColor)
    display   = widgets.ThemeFrame      (root,                                          column=1, row=0, border=True)
    shortcuts = widgets.ThemeButtonBar  (root, shortcutWidth, shortcutHeight, "Horizontal", shortcutCommands, buttonLabels=shortcutNames, column=1, row=1)
    appsBar   = widgets.ThemeProgressBar(root, sideBarWidth, sideBarHeight, "Vertical", column=2, row=0, rowspan=2, border=True, text=config.sideBarAppsLabel,  foreground=config.sideBarAppsColor)
    
    # Display Partitioning
    displayInteriorWidth   = displayWidth  - config.themePadding*4 # Interior and Exterior Padding
    displayInteriorHeight  = displayHeight - config.themePadding*4 # Interior and Exterior Padding
    rpmBarHeight           = config.rpmBarHeight
    rpmLabelsHeight        = config.rpmBarLabelHeight
    rpmDividerHeight       = config.themeBorderWidth
    speedHeight            = config.displayNumberHeight
    speedWidth             = config.displayNumberWidth
    infoPanelWidth         = config.infoPanelWidth
    infoPanelHeight        = config.infoPanelHeight
    torqueBarWidth         = config.torqueBarWidth
    torqueBarHeight        = config.torqueBarHeight
    torqueBarLabelHeight   = config.torqueBarLabelHeight
    verticalPaddingHeight  = (displayInteriorHeight - rpmBarHeight - rpmLabelsHeight - rpmDividerHeight - speedHeight - torqueBarHeight - torqueBarLabelHeight) / 2
    horizontalPaddingWidth = (displayInteriorWidth - speedWidth) / 2

    display.columnconfigure(0, minsize=horizontalPaddingWidth) # Padding  
    display.columnconfigure(1, minsize=speedWidth)             # Speed
    display.columnconfigure(2, minsize=horizontalPaddingWidth) # Padding

    display.rowconfigure   (0, minsize=rpmBarHeight)           # RPM Bar
    display.rowconfigure   (1, minsize=rpmDividerHeight)       # Divider
    display.rowconfigure   (2, minsize=rpmLabelsHeight)        # RPM Bar Labels
    display.rowconfigure   (3, minsize=verticalPaddingHeight)  # Padding
    display.rowconfigure   (4, minsize=speedHeight)            # Speed Display
    display.rowconfigure   (5, minsize=verticalPaddingHeight)  # Padding
    display.rowconfigure   (6, minsize=torqueBarLabelHeight)   # Torque Bar Labels
    display.rowconfigure   (7, minsize=torqueBarHeight)        # Torque Bar
    
    # Display Widgets
    global rpmBar
    global rpmLabels
    global infoPanel
    global speedStat
    global torqueBar

    rpmBar         = widgets.ThemeStrataBar(display, displayInteriorWidth, rpmBarHeight, "Horizontal", grid=True, column=0, row=0, columnspan=3, highlightPalette=config.rpmHighlight, lowlightPalette=config.rpmLowlight, paletteDomain=config.rpmDomain, maskLeft=5/6)
    rpmDivider     = widgets.ThemeDividerHorizontal(display, displayInteriorWidth,      column=0, row=1, columnspan=3)
    # rpmLabels      = widgets.LabelBarHorizontal(display, rpmBarWidth, rpmLabelsHeight,   column=0, row=2, columnspan=3, labelNames=config.rpmLabelValues, font=config.rpmBarFont)
    infoPanel      = widgets.ThemeFrame(display, grid=True, column=0, row=3, rowspan=3, sticky="W")
    speedStat      = widgets.ThemeLabelStat(display, grid=True, column=1, row=4,        sticky="S", font=config.themeFontExtraLarge)
    speedLabel     = widgets.ThemeLabel(display, grid=True, column=2, row=4,            sticky="SW", text=config.displayNumberSpeedText)
    torqueBarLabel = widgets.ThemeLabel(display, grid=True, column=1, row=6,            sticky="S",  text=config.torqueBarText, font=config.themeFontSmall)
    torqueBar      = widgets.ThemeProgressBar(display, torqueBarWidth, torqueBarHeight, "Horizontal", column=0, row=7, columnspan=3, border=True, foreground=config.themeBlue)

    # Info Panel Partitioning
    infoStatWidth     = config.infoPanelStatWidth
    infoDividerHeight = config.themeBorderWidth
    infoPaddingWidth  = config.infoPanelSidePadding
    infoLabelWidth    = infoPanelWidth - infoStatWidth - 2*infoPaddingWidth
    infoStatHeight    = (infoPanelHeight - 2*infoDividerHeight) / 4

    infoPanel.columnconfigure(0, minsize=infoPaddingWidth) # Padding
    infoPanel.columnconfigure(1, minsize=infoLabelWidth)   # Labels
    infoPanel.columnconfigure(2, minsize=infoStatWidth)    # Stats
    infoPanel.columnconfigure(3, minsize=infoPaddingWidth) # Padding

    infoPanel.rowconfigure(0, minsize=infoDividerHeight) # Divider
    infoPanel.rowconfigure(1, minsize=infoStatHeight)    # Charge
    infoPanel.rowconfigure(2, minsize=infoStatHeight)    # Temp 1
    infoPanel.rowconfigure(3, minsize=infoStatHeight)    # Temp 2
    infoPanel.rowconfigure(4, minsize=infoStatHeight)    # Temp 3
    infoPanel.rowconfigure(5, minsize=infoDividerHeight) # Divider
    
    # Info Panel Widgets
    global chargeStat
    global temp1Stat
    global temp2Stat
    global temp3Stat

    infoUpperDivider = widgets.ThemeDividerHorizontal(infoPanel, infoPanelWidth, grid=True, column=1, row=0, columnspan=2)
    chargeStat       = widgets.ThemeLabelStat(infoPanel, grid=True, column=2, row=1, sticky="E")
    temp1Stat        = widgets.ThemeLabelStat(infoPanel, grid=True, column=2, row=2, sticky="E")
    temp2Stat        = widgets.ThemeLabelStat(infoPanel, grid=True, column=2, row=3, sticky="E")
    temp3Stat        = widgets.ThemeLabelStat(infoPanel, grid=True, column=2, row=4, sticky="E")
    chargeLabel      = widgets.ThemeLabel(infoPanel, grid=True, column=1, row=1, text="SoC: ",    sticky="W")
    temp1Label       = widgets.ThemeLabel(infoPanel, grid=True, column=1, row=2, text="Temp 1: ", sticky="W")
    temp2Label       = widgets.ThemeLabel(infoPanel, grid=True, column=1, row=3, text="Temp 2: ", sticky="W")
    temp3Label       = widgets.ThemeLabel(infoPanel, grid=True, column=1, row=4, text="Temp 3: ", sticky="W")
    infoLowerDivider = widgets.ThemeDividerHorizontal(infoPanel, infoPanelWidth, grid=True, column=1, row=5, columnspan=2)

# Update
# - Sends current data to appropriate widgets
# - Can be called when view is open or closed
def Update():
    global brakeBar
    global appsBar
    global rpmBar
    global torqueBar
    global speedStat
    global chargeStat
    global temp1Stat
    global temp2Stat
    global temp3Stat

    brakeBar.Set  (car_data.brake1Percent       / 100)
    appsBar.Set   (car_data.apps1Percent        / 100)
    rpmBar.Set    (car_data.rpmPercent          / 100)
    torqueBar.Set (car_data.torquePercentageMax / 100)
    speedStat.Set (car_data.speedMph)
    chargeStat.Set(car_data.stateOfCharge)
    temp1Stat.Set (car_data.temp1)
    temp2Stat.Set (car_data.temp2)
    temp3Stat.Set (car_data.temp3)

# Open
# - Packs and updates the view
def Open():
    global root
    root.pack()
    # Update()

# Close
# - Unpacks the view
def Close():
    global root
    root.forget()