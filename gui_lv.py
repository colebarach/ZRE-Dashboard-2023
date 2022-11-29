# Includes
import config
import car_data
import lib_tkinter

def Initialize(gui):
    global root
    global message

    # Root Partitioning -----------------------------------------------------------------------------------
    root = lib_tkinter.DashFrame(gui, grid=False)
    root.grid_columnconfigure(0, minsize=config.SCREEN_W)
    root.grid_rowconfigure(0,    minsize=config.SCREEN_H)
    
    # Root Widgets ----------------------------------------------------------------------------------------
    message = lib_tkinter.DashLabel(root, font=config.lvFontSize)

def Update():
    global message
    if(car_data.driveState == car_data.DriveState.INITIALIZING):
        message['text'] = "Booting..."
    elif(car_data.driveState == car_data.DriveState.LV_DRIVEOFF):
        message['text'] = "Low Voltage is on.\n\nWhen ready, have an ESO\nturn on high voltage."
    elif(car_data.driveState == car_data.DriveState.HV_DRIVEOFF):
        message['text'] = "High Voltage is on.\n\nPress and hold the brake,\nthen press the start button."

def Open():
    root.pack()
    Update()

def Close():
    root.forget()