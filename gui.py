# Title: GUI Main
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: GUI main script. Responsible for initialization and management of the views of the dashboard.

# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

# Includes
import config
import car_data

import gui_lv
import gui_speed
import gui_endurance
import gui_calibration
import gui_bms
import gui_debug

views = [gui_lv, gui_speed, gui_endurance]
currentView = gui_lv

# GUI Initialization
def Initialize():
    global gui
    print("GUI - Initializing...")
    gui = Tk()
    gui.title("Dashboard 2023 - Rev.0")
    gui.geometry(str(config.SCREEN_W) + 'x' + str(config.SCREEN_H))
    gui.resizable(0, 0)

    gui_debug.Initialize(gui)

    InitializeViews()
    SetView()

    InitializeInterrupts()

    UpdateLoop()

# GUI Update Interrupt
def UpdateLoop():
    global gui
    currentView.Update()
    gui.after(100, UpdateLoop)

def Close():
    print("GUI - Closing...")
    global gui
    gui.destroy()

# Close all views
def ClearViews():
    for view in views:
        view.Close()

# Initialize all views
def InitializeViews():
    for view in views:
        view.Initialize(gui)

def SetView(view = currentView):
    global currentView
    print("GUI - Set View:", view.__name__)
    driveEnabled = car_data.driveState == car_data.DriveState.HV_DRIVEON
    if(not driveEnabled):
        currentView = gui_lv
    else:
        currentView = view
    currentView = view
    ClearViews()
    currentView.Open()

def UpdateDriveState():
    if(car_data.driveState == car_data.driveStatePrime): return
    
    car_data.driveStatePrime = car_data.driveState
    
    if(car_data.driveState == car_data.DriveState.HV_DRIVEON):   SetView(gui_speed)
    if(car_data.driveState == car_data.DriveState.HV_DRIVEOFF):  SetView(gui_lv)
    if(car_data.driveState == car_data.DriveState.LV_DRIVEOFF):  SetView(gui_lv)
    if(car_data.driveState == car_data.DriveState.INITIALIZING): SetView(gui_lv)

# Keyboard Input
def KeyInterrupt(event):
    if(event.keysym == "F2"): gui_debug.Toggle()

def InitializeInterrupts():
    gui.bind('<Key>', KeyInterrupt)

# GUI Main Loop
def Loop():
    global gui
    print("GUI - Loop Starting...")
    gui.mainloop()
    # TEMPORARY. FOR DEBUG PURPOSES ONLY
    import can
    can.Close()