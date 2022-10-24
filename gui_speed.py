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
import config
import widgets
import car_data

global open

def Initialize(guiRoot):
    # Root Declaration
    global root
    root = widgets.CreateFrame(guiRoot, grid=False)

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
    global brakeBar
    global appsBar
    global display
    global shortcuts
    brakeBar = widgets.ProgressBarVertical(root, sideBarWidth, sideBarHeight, column=0, rowspan=2, border=True, font=config.sideBarFont, lowlightColor=config.sideBarBrakeColor, text=config.sideBarBrakeLabel)
    appsBar  = widgets.ProgressBarVertical(root, sideBarWidth, sideBarHeight, column=2, rowspan=2, border=True, font=config.sideBarFont, lowlightColor=config.sideBarAppsColor,  text=config.sideBarAppsLabel)
    display  = widgets.CreateFrame(root, column=1, row=0, border=True)
    
    # Shortcut Layout
    shortcutLambdas = [lambda: print("Open Endurance View"), lambda: print("Open Lap View"), lambda: print("Open Testing View"), lambda: print("Open Settings")]
    shortcutNames = ["Endurance\nView", "Lap\nView", "Testing\nView", "Settings"]
    
    shortcuts = widgets.ButtonBarHorizontal(root, shortcutWidth, shortcutHeight, shortcutLambdas, column=1, row=1, buttonNames=shortcutNames, font=config.shortcutBarFont)
     
    # Display Partitioning
    displayInteriorWidth   = displayWidth  - config.padding*4
    displayInteriorHeight  = displayHeight - config.padding*4
    rpmBarWidth            = displayInteriorWidth - config.padding*2
    rpmBarHeight           = config.rpmBarHeight
    rpmLabelsHeight        = config.rpmBarLabelHeight
    rpmDividerHeight       = config.borderWidth
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

    rpmBar         = widgets.StratifiedBarHorizontal(display, rpmBarWidth, rpmBarHeight, column=0, row=0, columnspan=3, maskLeft=60, maskRight=0, rangeColorsHigh=config.rpmHighColors, rangeColorsLow=config.rpmLowColors, rangeValues=config.rpmRanges)
    rpmDivider     = widgets.CreateDividerHorizontal(display, displayInteriorWidth,      column=0, row=1, columnspan=3)
    rpmLabels      = widgets.LabelBarHorizontal(display, rpmBarWidth, rpmLabelsHeight,   column=0, row=2, columnspan=3, labelNames=config.rpmLabelValues, font=config.rpmBarFont)
    infoPanel      = widgets.CreateFrame(display, column=0, row=3, rowspan=3, grid=True, sticky="W")
    speedStat      = widgets.CreateLabel(display, column=1, row=4, grid=True, font=config.displayNumberStatFont, sticky="S")
    speedLabel     = widgets.CreateLabel(display, column=2, row=4, grid=True, text=config.displayNumberSpeedText, font=config.displayNumberLabelFont, sticky="SW")
    torqueBarLabel = widgets.CreateLabel(display, column=1, row=6, grid=True, text=config.torqueBarText, font=config.torqueBarTextFont)
    torqueBar      = widgets.ProgressBarHorizontal(display, torqueBarWidth, torqueBarHeight, column=0, row=7, columnspan=3, border=True, lowlightColor=config.torqueBarColor)

    # Info Panel Partitioning
    infoStatWidth     = config.infoPanelStatWidth
    infoDividerHeight = config.borderWidth
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
    global chargeValue
    global temp1Value
    global temp2Value
    global temp3Value

    infoUpperDivider = widgets.CreateDividerHorizontal(infoPanel, infoPanelWidth, grid=True, column=1, row=0, columnspan=2)
    chargeValue      = widgets.CreateLabel(infoPanel, grid=True, column=2, row=1, font=config.infoPanelStatFont, sticky="E")
    temp1Value       = widgets.CreateLabel(infoPanel, grid=True, column=2, row=2, font=config.infoPanelStatFont, sticky="E")
    temp2Value       = widgets.CreateLabel(infoPanel, grid=True, column=2, row=3, font=config.infoPanelStatFont, sticky="E")
    temp3Value       = widgets.CreateLabel(infoPanel, grid=True, column=2, row=4, font=config.infoPanelStatFont, sticky="E")
    chargeLabel      = widgets.CreateLabel(infoPanel, grid=True, column=1, row=1, text="SoC: ",    font=config.infoPanelLabelFont, sticky="W")
    temp1Label       = widgets.CreateLabel(infoPanel, grid=True, column=1, row=2, text="Temp 1: ", font=config.infoPanelLabelFont, sticky="W")
    temp2Label       = widgets.CreateLabel(infoPanel, grid=True, column=1, row=3, text="Temp 2: ", font=config.infoPanelLabelFont, sticky="W")
    temp3Label       = widgets.CreateLabel(infoPanel, grid=True, column=1, row=4, text="Temp 3: ", font=config.infoPanelLabelFont, sticky="W")
    infoLowerDivider = widgets.CreateDividerHorizontal(infoPanel, infoPanelWidth, grid=True, column=1, row=5, columnspan=2)

def Update():
    brakeBar.SetBar(car_data.brake1Percent)
    appsBar.SetBar(car_data.apps1Percent)
    rpmBar.SetBar(car_data.rpmPercent)
    torqueBar.SetBar(car_data.torquePercent)
    speedStat['text']   = car_data.speed
    chargeValue['text'] = car_data.stateOfCharge
    temp1Value['text']  = car_data.temp1
    temp2Value['text']  = car_data.temp2
    temp3Value['text']  = car_data.temp3
    chargeValue['foreground'] = config.colorGreen
    temp1Value['foreground']  = config.GetTemperatureColor(car_data.temp1)
    temp2Value['foreground']  = config.GetTemperatureColor(car_data.temp2)
    temp3Value['foreground']  = config.GetTemperatureColor(car_data.temp3)

def Open():
    global open
    open = True
    root.pack()
    Update()

def Close():
    global open
    open = False
    root.forget()