# Title: GUI BMS View
# Author: Cole Barach
# Date Created: 22.11.19
# Date Updated: 22.11.25
# Function: BMS GUI View based on the BMS Monitoring System authored by Derek Dunn.

# Includes
import config
import lib_tkinter
import car_data

CELL_WIDTH_COUNT  = 18
CELL_HEIGHT_COUNT = 5

TEMP_WIDTH_COUNT = 9
TEMP_HEIGHT_COUNT = 5

# Initialization
# - Creates instances of all necessary widgets
# - Should only be called once per session
def Initialize(guiRoot):
    # Root --------------------------------------------------------------------------------------------------------------------------------------------------------
    global root
    root = lib_tkinter.DashFrame(guiRoot, grid=False)
    
    # Global Data
    global cellStats
    global canStatusStat
    global selfTestStat
    global voltageTestStat
    global tempTestStat
    global senseTestStat

    # Partitioning
    rootWidth          = config.SCREEN_W
    rootHeight         = config.SCREEN_H
    statPanelWidth     = rootWidth
    statPanelHeight    = config.bmsStatPanelHeight
    buttonPanelWidth   = rootWidth
    buttonPanelHeight  = config.bmsButtonPanelHeight
    cellPanelWidth     = rootWidth
    cellPanelHeight    = rootHeight - statPanelHeight - buttonPanelHeight

    root.columnconfigure(0, minsize=rootWidth)
    root.rowconfigure   (0, minsize=statPanelHeight)
    root.rowconfigure   (1, minsize=cellPanelHeight)
    root.rowconfigure   (2, minsize=buttonPanelHeight)

    # Setup
    buttonCommands = [lambda: SetViewType("Cell"), lambda: SetViewType("Voltage"), lambda: SetViewType("Temperature"), lambda: SetViewType("Delta")]
    buttonLabels   = ["Cell\nView", "Voltage\nView", "Temperature\nView", "Delta\nView"]

    # Widgets
    statPanel   = lib_tkinter.DashFrame(root, column=0, row=0)
    cellPanel   = lib_tkinter.DashFrame(root, column=0, row=1, columnspan=2)
    buttonPanel = lib_tkinter.DashButtonBar(root, buttonPanelWidth, buttonPanelHeight, "Horizontal", buttonCommands, buttonLabels=buttonLabels, column=0, row=2)

    # Cell Panel --------------------------------------------------------------------------------------------------------------------------------------------------
    cellStats = [None]*(CELL_WIDTH_COUNT*CELL_HEIGHT_COUNT)
    
    # Partitioning
    cellPanelInteriorWidth  = config.bmsCellPanelWidth
    cellPanelInteriorHeight = config.bmsCellPanelHeight
    cellStatWidth  = int(cellPanelInteriorWidth  / CELL_WIDTH_COUNT)
    cellStatHeight = int(cellPanelInteriorHeight / CELL_HEIGHT_COUNT)

    # Widgets
    for x in range(CELL_WIDTH_COUNT):
        for y in range(CELL_HEIGHT_COUNT):
            index = x + y*CELL_WIDTH_COUNT
            cellPanel.columnconfigure(x, minsize=cellStatWidth)
            cellPanel.rowconfigure   (y, minsize=cellStatHeight)
            cellStats[index] = lib_tkinter.DashBmsCellStat(cellPanel, cellStatWidth-2, cellStatHeight-2, column=x, row=y)

    # Stat Panel --------------------------------------------------------------------------------------------------------------------------------------------------
    # Partitioning
    statPanelInteriorWidth  = statPanelWidth  - 2*config.dashPadding - 2*config.dashBorderWidth
    statPanelInteriorHeight = statPanelHeight - 2*config.dashPadding - 2*config.dashBorderWidth
    statHeight      = statPanelInteriorHeight / 5
    faultStatWidth  = statHeight
    faultLabelWidth = config.bmsFaultCodeWidth - faultStatWidth

    statPanel.columnconfigure(0, minsize=faultLabelWidth)
    statPanel.columnconfigure(1, minsize=faultStatWidth)
    statPanel.columnconfigure(2, minsize=statPanelInteriorWidth - faultLabelWidth - faultStatWidth)
    statPanel.rowconfigure   (0, minsize=statHeight)
    statPanel.rowconfigure   (1, minsize=statHeight)
    statPanel.rowconfigure   (2, minsize=statHeight)
    statPanel.rowconfigure   (3, minsize=statHeight)
    statPanel.rowconfigure   (4, minsize=statHeight)

    # Widgets
    canStatusLabel   = lib_tkinter.DashLabel    (statPanel, column=0, row=0, sticky="E", text="CAN Status:",   font=config.dashFontSmall)
    selfTestLabel    = lib_tkinter.DashLabel    (statPanel, column=0, row=1, sticky="E", text="Self-Test:",    font=config.dashFontSmall)
    voltageTestLabel = lib_tkinter.DashLabel    (statPanel, column=0, row=2, sticky="E", text="Voltages:",     font=config.dashFontSmall)
    tempTestLabel    = lib_tkinter.DashLabel    (statPanel, column=0, row=3, sticky="E", text="Temperatures:", font=config.dashFontSmall)
    senseTestLabel   = lib_tkinter.DashLabel    (statPanel, column=0, row=4, sticky="E", text="Sense Lines:",  font=config.dashFontSmall)
    canStatusStat    = lib_tkinter.DashCheckStat(statPanel, column=1, row=0, sticky="W")
    selfTestStat     = lib_tkinter.DashCheckStat(statPanel, column=1, row=1, sticky="W", inverted=True)
    voltageTestStat  = lib_tkinter.DashCheckStat(statPanel, column=1, row=2, sticky="W", inverted=True)
    tempTestStat     = lib_tkinter.DashCheckStat(statPanel, column=1, row=3, sticky="W", inverted=True)
    senseTestStat    = lib_tkinter.DashCheckStat(statPanel, column=1, row=4, sticky="W", inverted=True)

def SetViewType(viewType):
    for stat in cellStats:
        stat.SetViewType(viewType)

# Update
# - Sends current data to appropriate widgets
# - Can be called when view is open or closed
def Update():
    global cellStats
    global selfTestStat
    global voltageTestStat
    global tempTestStat
    global senseTestStat
    for index in range(CELL_WIDTH_COUNT*CELL_HEIGHT_COUNT):
        cellStats[index].Set(car_data.cellVoltages[index], car_data.cellBalancings[index], car_data.packTemperatures[int(index/2)])
        cellStats[index].SetLowest(car_data.cellVoltageMin)
    canStatusStat.Set  (car_data.bmsCanActive)
    selfTestStat.Set   (car_data.errorBmsSelfTestFault)
    voltageTestStat.Set(car_data.errorBmsVoltageFault)
    tempTestStat.Set   (car_data.errorBmsTempFault)
    senseTestStat.Set  (car_data.errorBmsSenseLineFault)

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