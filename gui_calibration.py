# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

import enum
from enum import Enum

# Includes
import config
import car_data
import widgets

# Calibration States
#   Start - Buffer menu to avoid accidental calibration
#   Request_Pedals_None - For minimum values, tells the driver to not touch pedals
#   Request_Pedals_APPS - For maximum values, tells the driver to press throttle
#   Finished - For valid calibration only
#   Failed - When calibration values were invalid
class CalibrationState(Enum):
    START                = 0,
    REQUEST_PEDALS_NONE  = 1,
    REQUEST_PEDALS_APPS  = 2,
    FINISHED             = 3,
    FAILED               = 4
calibrationState = CalibrationState.START

# Current Calibration Values
#   Will be reset when exiting calibration mode
apps1CurrentMax     = 0
apps2RawCurrentMax  = 0
apps1CurrentMin     = 0
apps2RawCurrentMin  = 0

# GUI Initialization
def Initialize(gui):
    global root
    global message
    global open
    
    open = False
    root = widgets.CreateFrame(gui, grid=False)
    root.grid_columnconfigure(0, minsize=config.SCREEN_W)
    root.grid_rowconfigure(0,    minsize=config.SCREEN_H)
    message = widgets.CreateLabel(root)
    message.grid()

# GUI Update Interrupt
def Update():
    global calibrationState
    global open

    # Check if open
    if(not open): return
    if(calibrationState == CalibrationState.START):
        # Start Menu
        message['text'] = "Press button 1 to start calibration"
    elif(calibrationState == CalibrationState.REQUEST_PEDALS_NONE):
        # No Pedals Menu
        message['text'] = "Release both pedals then press button 1"
    elif(calibrationState == CalibrationState.REQUEST_PEDALS_APPS):
        # APPS Pedal Menu
        message['text'] = "Press the throttle fully then press button 1"
    elif(calibrationState == CalibrationState.FINISHED):
        # Finished Menu
        message['text'] = "Calibration Finshed"
    elif(calibrationState == CalibrationState.FAILED):
        # Failed Menu
        message['text'] = "Calibration Failed"

# GUI Open Interrupt
def Open():
    global open
    open = True
    root.pack()
    Update()

# GUI Close Interrupt
def Close():
    global open
    global calibrationState

    open = False
    root.forget()
    calibrationState = CalibrationState.START

    global apps1CurrentMax
    global apps2RawCurrentMax

def ButtonInterrupt(button):
    global calibrationState
    global apps1CalibrationMax
    global apps2RawCalibrationMax
    global apps1CalibrationMin
    global apps2RawCalibrationMin
    
    if(button == 1):
        calibrationState = CalibrationState.START
    if(button == 0):
        if(calibrationState == CalibrationState.START):
            calibrationState = CalibrationState.REQUEST_PEDALS_NONE

        elif(calibrationState == CalibrationState.REQUEST_PEDALS_NONE):
            apps1CalibrationMin    = car_data.apps1
            apps2RawCalibrationMin = car_data.apps2Raw
            calibrationState = CalibrationState.REQUEST_PEDALS_APPS

        elif(calibrationState == CalibrationState.REQUEST_PEDALS_APPS):
            apps1CalibrationMax    = car_data.apps1
            apps2RawCalibrationMax = car_data.apps2Raw
            ValidateCalibration()
            ApplyCalibration()
    Update()

def ValidateCalibration():
    global calibrationState
    global apps1CalibrationMax
    global apps2RawCalibrationMax
    global apps1CalibrationMin
    global apps2RawCalibrationMin

    calibrationState = CalibrationState.FAILED
    if(apps1CalibrationMax    <= apps1CalibrationMin):    return
    if(apps2RawCalibrationMax <= apps2RawCalibrationMin): return
    calibrationState = CalibrationState.FINISHED

def ApplyCalibration():
    global calibrationState
    global apps1CalibrationMax
    global apps2RawCalibrationMax
    global apps1CalibrationMin
    global apps2RawCalibrationMin

    if(calibrationState != CalibrationState.FINISHED): return
    car_data.apps1Max    = apps1CalibrationMax
    car_data.apps2RawMax = apps2RawCalibrationMax
    car_data.apps1Min    = apps1CalibrationMin
    car_data.apps2RawMin = apps2RawCalibrationMin