# Title: GUI Main
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: GUI main script. Responsible for initialization and management of the views of the dashboard.

# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

import enum
from enum import Enum

# Includes
import main
import config
import car_data

import gui_lv
import gui_speed
import gui_endurance
import gui_lap
import gui_testing
import gui_calibration

views = [gui_lv, gui_speed]
currentView = gui_lv

# GUI Initialization
def Initialize():
    global gui
    gui = Tk()
    gui.title("Dashboard 2023 - Rev.0")
    gui.geometry(str(config.SCREEN_W) + 'x' + str(config.SCREEN_H))
    gui.resizable(0, 0)

    InitializeViews() 
    SetView(gui_speed)
    
    InitializeInterrupts()
    Update()

# GUI Update Interrupt
def Update():
    currentView.Update()

# Close all views
def ClearViews():
    for view in views:
        view.Close()

# Initialize all views
def InitializeViews():
    for view in views:
        view.Initialize(gui)

def SetView(view):
    global currentView
    driveEnabled = car_data.driveState == car_data.DriveState.HV_DRIVEON
    if(not driveEnabled):
        currentView = gui_lv
    else:
        currentView = view
    ClearViews()
    currentView.Open()

# Temporary keyboard interrupts
def KeyInterrupt(event):
    global currentView
    if(event.char == '1'):
        main.SetDriveState(car_data.DriveState.INITIALIZING)
        SetView(gui_lv)
    if(event.char == '2'):
        main.SetDriveState(car_data.DriveState.LV_DRIVEOFF)
        SetView(gui_lv)
    if(event.char == '3'):
        main.SetDriveState(car_data.DriveState.HV_DRIVEOFF)
        SetView(gui_lv)
    if(event.char == '4'):
        main.SetDriveState(car_data.DriveState.HV_DRIVEON)
        SetView(gui_speed)
    if(event.char == '5'):
        0
        # gui_calibration.ButtonInterrupt(0)
    if(event.char == '6'):
        0
        # gui_calibration.ButtonInterrupt(1)
    if(event.char == '7'):
        0
    if(event.char == '8'):
        0
    if(event.char == '9'):
        0
    if(event.char == '0'):
        0
    Update()

def InitializeInterrupts():
    gui.bind("1", KeyInterrupt)
    gui.bind("2", KeyInterrupt)
    gui.bind("3", KeyInterrupt)
    gui.bind("4", KeyInterrupt)
    gui.bind("5", KeyInterrupt)
    gui.bind("6", KeyInterrupt)
    gui.bind("7", KeyInterrupt)
    gui.bind("8", KeyInterrupt)
    gui.bind("9", KeyInterrupt)
    gui.bind("0", KeyInterrupt)

# GUI Main Loop
def Loop():
    gui.mainloop()