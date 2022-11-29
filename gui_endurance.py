# Title: GUI Edurance View
# Author: Cole Barach
# Date Created: 22.11.23
# Date Updated: 22.11.23
# Function: Basic Driving View for the GUI. Displays speed and basic info.

# Includes
import gui
import gui_speed
import config
import lib_tkinter
import car_data

# Initialization
# - Creates instances of all necessary widgets
# - Should only be called once per session
def Initialize(guiRoot):
    # Root --------------------------------------------------------------------------------------------------------------------------------------------------------
    global root
    root = lib_tkinter.DashFrame(guiRoot, grid=False)

    # Partitioning
    rootWidth       = config.SCREEN_W
    rootHeight      = config.SCREEN_H
    brakeBarWidth   = config.driveSideBarWidth
    appsBarWidth    = config.driveSideBarWidth
    buttonBarHeight = config.driveButtonBarHeight
    displayWidth    = rootWidth - brakeBarWidth - appsBarWidth
    displayHeight   = rootHeight - buttonBarHeight
    
    root.columnconfigure(0, minsize=brakeBarWidth)
    root.columnconfigure(1, minsize=displayWidth)
    root.columnconfigure(2, minsize=appsBarWidth)
    root.rowconfigure   (0, minsize=displayHeight)
    root.rowconfigure   (1, minsize=buttonBarHeight)

    # Global Widgets
    global brakeBar
    global appsBar
    global rpmBar
    global torqueBar
    global regenBar
    global chargeStat
    global temp1Stat
    global temp2Stat
    global temp3Stat
    global temp4Stat
    global temp5Stat

    # Widget Setup
    buttonLabels   = ["Speed\nView", "Endurance\nView", "Lap\nView", "Settings"]
    buttonCommands = [lambda: gui.SetView(gui_speed),0,0,0]

    # Widgets
    brakeBar  = lib_tkinter.DashProgressBar(root, brakeBarWidth,  rootHeight, "Vertical", column=0, row=0, rowspan=2, scaleFactor=100, text="BRAKE",    foreground=config.brakeColor, font=config.driveSideBarFont, border=True)
    appsBar   = lib_tkinter.DashProgressBar(root, appsBarWidth,   rootHeight, "Vertical", column=2, row=0, rowspan=2, scaleFactor=100, text="THROTTLE", foreground=config.appsColor, font=config.driveSideBarFont, border=True)
    buttonBar = lib_tkinter.DashButtonBar  (root, displayWidth, buttonBarHeight, "Horizontal", buttonCommands, buttonLabels, column=1, row=1, font=config.driveButtonBarFont, border=True)
    display   = lib_tkinter.DashFrame      (root, column=1, row=0, border=True)
    
    # Display -----------------------------------------------------------------------------------------------------------------------------------------------------
    # Partitioning
    displayInteriorWidth  = displayWidth  - 4*config.dashPadding - 2*config.dashBorderWidth
    displayInteriorHeight = displayHeight - 4*config.dashPadding - 2*config.dashBorderWidth
    rpmPanelHeight        = config.driveTopBarHeight
    torquePanelHeight     = config.driveBottomBarLabelHeight
    regenPanelHeight      = config.driveBottomBarLabelHeight
    speedStatWidth        = config.driveCenterPanelStatWidth
    speedStatHeight       = displayInteriorHeight - rpmPanelHeight - torquePanelHeight - regenPanelHeight
    statPanelWidth        = int((displayInteriorWidth - speedStatWidth) / 2)
    statPanelHeight       = config.driveSidePanelHeight
    speedLabelWidth       = statPanelWidth
    speedLabelHeight      = config.driveCenterPanelStatHeight

    display.columnconfigure(0, minsize=statPanelWidth)
    display.columnconfigure(1, minsize=speedStatWidth)
    display.columnconfigure(2, minsize=speedLabelWidth)

    display.rowconfigure   (0, minsize=rpmPanelHeight)
    display.rowconfigure   (1, minsize=speedStatHeight)
    display.rowconfigure   (2, minsize=regenPanelHeight)
    display.rowconfigure   (3, minsize=torquePanelHeight)

    # Widgets
    rpmPanel     = lib_tkinter.DashFrame      (display, column=0, row=0, columnspan=3)
    regenPanel   = lib_tkinter.DashFrame      (display, column=0, row=2, columnspan=3)
    torquePanel  = lib_tkinter.DashFrame      (display, column=0, row=3, columnspan=3)
    statPanel    = lib_tkinter.DashFrame      (display, column=0, row=1, sticky="W")
    chargeStat   = lib_tkinter.DashLabelStat  (display, column=1, row=1, font=config.driveCenterPanelStatFont)
    chargeLabel  = lib_tkinter.DashLabelCanvas(display, speedLabelWidth, speedLabelHeight, 40, speedLabelHeight - 16, column=2, row=1, text="SoC", font=config.driveCenterPanelLabelFont)

    # RPM Panel ---------------------------------------------------------------------------------------------------------------------------------------------------
    # Partitioning
    rpmDividerHeight = config.dashBorderWidth
    rpmBarHeight     = rpmPanelHeight - rpmDividerHeight
    # Widgets
    rpmBar     = lib_tkinter.DashStrataBar(rpmPanel, displayInteriorWidth, rpmBarHeight, "Horizontal", scaleFactor=config.RPM_MAX, highlightPalette=config.rpmHighlight, lowlightPalette=config.rpmLowlight, paletteDomain=config.rpmDomain, column=0, row=0, maskLeft=2/3, maskRight=0)
    rpmDivider = lib_tkinter.DashDivider  (rpmPanel, displayInteriorWidth,               "Horizontal", column=0, row=1)

    # Torque Panel ------------------------------------------------------------------------------------------------------------------------------------------------
    # Partitioning
    torqueBarLabelWidth  = config.driveBottomBarLabelWidth
    torqueBarLabelHeight = config.driveBottomBarLabelHeight
    torqueBarWidth       = displayInteriorWidth - torqueBarLabelWidth
    torqueBarHeight      = config.driveBottomBarHeight
    torquePanel.columnconfigure(0, minsize=torqueBarWidth)
    torquePanel.columnconfigure(1, minsize=torqueBarLabelWidth)
    torquePanel.rowconfigure   (0, minsize=torqueBarHeight)
    # Widgets
    torqueBar   = lib_tkinter.DashProgressBar(torquePanel, torqueBarWidth, torqueBarHeight, "Horizontal", column=0, row=0, scaleFactor=100, foreground=config.torqueColor, border=True, borderWidth=config.dashBorderLight, highlight=config.dashLowlight)
    torqueLabel = lib_tkinter.DashLabelCanvas(torquePanel, torqueBarLabelWidth, torqueBarLabelHeight, torqueBarLabelWidth/2, torqueBarLabelHeight/2, column=1, row=0, text="T", font=config.driveBottomBarLabelFont)
    
    # Regen Panel -------------------------------------------------------------------------------------------------------------------------------------------------
    # Partitioning
    regenBarLabelWidth  = config.driveBottomBarLabelWidth
    regenBarLabelHeight = config.driveBottomBarLabelHeight
    regenBarWidth       = displayInteriorWidth - regenBarLabelWidth
    regenBarHeight      = config.driveBottomBarHeight
    regenPanel.columnconfigure(0, minsize=regenBarWidth)
    regenPanel.columnconfigure(1, minsize=regenBarLabelWidth)
    regenPanel.rowconfigure   (0, minsize=regenBarHeight)
    # Widgets
    regenBar   = lib_tkinter.DashProgressBar(regenPanel, regenBarWidth, regenBarHeight, "Horizontal", column=0, row=0, scaleFactor=100, foreground=config.regenColor, border=True, borderWidth=config.dashBorderLight, highlight=config.dashLowlight)
    regenLabel = lib_tkinter.DashLabelCanvas(regenPanel, regenBarLabelWidth, regenBarLabelHeight, regenBarLabelWidth/2, regenBarLabelHeight/2, column=1, row=0, text="R", font=config.driveBottomBarLabelFont)

    # Stat Panel --------------------------------------------------------------------------------------------------------------------------------------------------
    # Partitioning
    statPanelInteriorWidth  = config.driveSidePanelWidth
    statPanelDividerHeight  = config.dashBorderWidth
    statPanelInteriorHeight = statPanelHeight - 2*statPanelDividerHeight
    statWidth               = config.driveSidePanelStatHeight
    statHeight              = int(statPanelInteriorHeight / 4)
    statLabelWidth          = statPanelInteriorWidth - statWidth

    statPanel.columnconfigure(0, minsize=statLabelWidth)
    statPanel.columnconfigure(1, minsize=statWidth)
    statPanel.rowconfigure   (0, minsize=statPanelDividerHeight)
    statPanel.rowconfigure   (1, minsize=statHeight)
    statPanel.rowconfigure   (2, minsize=statHeight)
    statPanel.rowconfigure   (3, minsize=statHeight)
    statPanel.rowconfigure   (4, minsize=statHeight)
    statPanel.rowconfigure   (5, minsize=statHeight)
    statPanel.rowconfigure   (6, minsize=statPanelDividerHeight)

    # Widgets
    statPanelDividerTop     = lib_tkinter.DashDivider  (statPanel, statPanelInteriorWidth, "Horizontal", column=0, row=0, columnspan=2)
    temp1Stat               = lib_tkinter.DashLabelStat(statPanel, column=1, row=1, sticky="E", font=config.driveSidePanelStatFont, paletteDomain=config.tempDomain, highlightPalette=config.tempHighlight)
    temp2Stat               = lib_tkinter.DashLabelStat(statPanel, column=1, row=2, sticky="E", font=config.driveSidePanelStatFont, paletteDomain=config.tempDomain, highlightPalette=config.tempHighlight)
    temp3Stat               = lib_tkinter.DashLabelStat(statPanel, column=1, row=3, sticky="E", font=config.driveSidePanelStatFont, paletteDomain=config.tempDomain, highlightPalette=config.tempHighlight)
    temp4Stat               = lib_tkinter.DashLabelStat(statPanel, column=1, row=4, sticky="E", font=config.driveSidePanelStatFont, paletteDomain=config.tempDomain, highlightPalette=config.tempHighlight)
    temp5Stat               = lib_tkinter.DashLabelStat(statPanel, column=1, row=5, sticky="E", font=config.driveSidePanelStatFont, paletteDomain=config.tempDomain, highlightPalette=config.tempHighlight)
    temp1Label              = lib_tkinter.DashLabel    (statPanel, column=0, row=1, sticky="W", font=config.driveSidePanelLabelFont, text="Temp 1:")
    temp2Label              = lib_tkinter.DashLabel    (statPanel, column=0, row=2, sticky="W", font=config.driveSidePanelLabelFont, text="Temp 2:")
    temp3Label              = lib_tkinter.DashLabel    (statPanel, column=0, row=3, sticky="W", font=config.driveSidePanelLabelFont, text="Temp 3:")
    temp4Label              = lib_tkinter.DashLabel    (statPanel, column=0, row=4, sticky="W", font=config.driveSidePanelLabelFont, text="Temp 4:")
    temp5Label              = lib_tkinter.DashLabel    (statPanel, column=0, row=5, sticky="W", font=config.driveSidePanelLabelFont, text="Temp 5:")
    statPanelDividerBottom  = lib_tkinter.DashDivider  (statPanel, statPanelInteriorWidth, "Horizontal", column=0, row=6, columnspan=2)

# Update
# - Sends current data to appropriate widgets
# - Can be called when view is open or closed
def Update():
    global brakeBar
    global appsBar
    global rpmBar
    global torqueBar
    global regenBar
    global speedStat
    global chargeStat
    global temp1Stat
    global temp2Stat
    global temp3Stat

    brakeBar.Set  (car_data.brake1Percent)
    appsBar.Set   (car_data.apps1Percent)
    rpmBar.Set    (car_data.rpm)
    torqueBar.Set (car_data.torquePercentageMax)
    regenBar.Set  (car_data.torquePercentageRegen)
    chargeStat.Set(car_data.stateOfCharge)
    temp1Stat.Set (car_data.temp1)
    temp2Stat.Set (car_data.temp2)
    temp3Stat.Set (car_data.temp3)
    temp3Stat.Set (car_data.temp3)
    temp3Stat.Set (car_data.temp3)

# Open
# - Packs and updates the view
def Open():
    global root
    root.pack()

# Close
# - Unpacks the view
def Close():
    global root
    root.forget()