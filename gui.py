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
import can

import gui_lv
import gui_speed
import gui_endurance
import gui_lap
import gui_testing
import gui_calibration
import gui_debug

views = [gui_lv, gui_speed]
currentView = gui_speed

# GUI Initialization
def Initialize():
    global gui
    print("GUI - Initializing...")
    gui = Tk()
    gui.title("Dashboard 2023 - Rev.0")
    gui.geometry(str(config.SCREEN_W) + 'x' + str(config.SCREEN_H))
    gui.resizable(0, 0)

    # InitializeInterrupts()

    gui_debug.Initialize(gui)
    gui_speed.Initialize(gui)
    gui_speed.Open()
    currentView = gui_speed
    
    # InitializeViews()
    # SetView()
    Update()

# GUI Update Interrupt
def Update():
    global gui
    currentView.Update()
    gui.after(10, Update)

def Close():
    print("GUI - Closing...")
    global gui
    gui.destroy()

# # Close all views
# def ClearViews():
#     for view in views:
#         view.Close()

# # Initialize all views
# def InitializeViews():
#     for view in views:
#         view.Initialize(gui)

# def SetView(view = currentView):
#     global currentView
#     print("GUI - Set View:", view.__name__)
#     driveEnabled = car_data.driveState == car_data.DriveState.HV_DRIVEON
#     if(not driveEnabled):
#         currentView = gui_lv
#     else:
#         currentView = view
#     currentView = view
#     ClearViews()
#     currentView.Open()

# def UpdateDriveState():
#     if(car_data.driveState == car_data.driveStatePrime): return
#     car_data.driveStatePrime = car_data.driveState
#     if(car_data.driveState == car_data.DriveState.HV_DRIVEON):   SetView(gui_speed)
#     if(car_data.driveState == car_data.DriveState.HV_DRIVEOFF):  SetView(gui_lv)
#     if(car_data.driveState == car_data.DriveState.LV_DRIVEOFF):  SetView(gui_lv)
#     if(car_data.driveState == car_data.DriveState.INITIALIZING): SetView(gui_lv)
#     Update()

# # Temporary keyboard interrupts
# def KeyInterrupt(event):
#     global currentView
#     if(event.char == '1'):
#         car_data.driveState = car_data.DriveState.INITIALIZING
#         SetView(gui_lv)
#     if(event.char == '2'):
#         car_data.driveState = car_data.DriveState.LV_DRIVEOFF
#         SetView(gui_lv)
#     if(event.char == '3'):
#         car_data.driveState = car_data.DriveState.HV_DRIVEOFF
#         SetView(gui_lv)
#     if(event.char == '4'):
#         car_data.driveState = car_data.DriveState.HV_DRIVEON
#         SetView(gui_speed)
#     if(event.char == '5'):
#         SetView(gui_calibration)
#     if(event.char == '6'):
#         gui_calibration.InputInterrupt(0)
#     if(event.char == '7'):
#         gui_calibration.InputInterrupt(1)
#     if(event.char == '8'):
#         car_data.apps1Min = 50
#         car_data.apps1Max = 480
#         car_data.apps2RawMin = 70
#         car_data.apps2RawMax = 710
#         can.SendCommandAppsCalibration()
#     if(event.char == '9'):
#         0
#     if(event.char == '0'):
#         0
#     if(event.char == 'q'):
#         main.Close()

# def InitializeInterrupts():
#     gui.bind('1', KeyInterrupt)
#     gui.bind('2', KeyInterrupt)
#     gui.bind('3', KeyInterrupt)
#     gui.bind('4', KeyInterrupt)
#     gui.bind('5', KeyInterrupt)
#     gui.bind('6', KeyInterrupt)
#     gui.bind('7', KeyInterrupt)
#     gui.bind('8', KeyInterrupt)
#     gui.bind('9', KeyInterrupt)
#     gui.bind('0', KeyInterrupt)
#     gui.bind('q', KeyInterrupt)

# GUI Main Loop
def Loop():
    global gui
    print("GUI - Loop Starting...")
    gui.mainloop()