# Libraries
import enum
from enum import Enum

# Includes
import config
import car_data
import lib_tkinter
import can

# Calibration States
#   Start               - Buffer menu to avoid accidental calibration
#   Request_Pedals_None - For minimum values, tells the driver to not touch pedals
#   Request_Pedals_APPS - For maximum values, tells the driver to press throttle
#   Finished            - For valid calibration only
#   Failed              - When calibration values were invalid
class CalibrationState(Enum):
    START                = 0,
    REQUEST_APPS_MIN     = 1,
    REQUEST_APPS_MAX     = 2,
    FINISHED             = 3,
    FAILED               = 4
calibrationState = CalibrationState.START

# Current Calibration Values
# - Will be reset when exiting calibration mode
apps1CurrentMin     = 0
apps1CurrentMax     = 0
apps2RawCurrentMin  = 0
apps2RawCurrentMax  = 0

# View Initialization
# - Call before using any other functions
def Initialize(gui):
    global root
    global message
    global open
    
    open = False
    root = lib_tkinter.DashFrame(gui, grid=False)
    root.grid_columnconfigure(0, minsize=config.SCREEN_W)
    root.grid_rowconfigure(0,    minsize=config.SCREEN_H)
    message = lib_tkinter.DashLabel(root)
    message.grid()

# View Update Interrupt
def Update():
    global calibrationState
    global open
    global message

    if(calibrationState == CalibrationState.START):
        # Start Menu
        message['text'] = "Press button 1 to start calibration"
    elif(calibrationState == CalibrationState.REQUEST_APPS_MIN):
        # No Pedals Menu
        message['text'] = "Release both pedals, then press button 1"
    elif(calibrationState == CalibrationState.REQUEST_APPS_MAX):
        # APPS Pedal Menu
        message['text'] = "Press the throttle fully, then press button 1"
    elif(calibrationState == CalibrationState.FINISHED):
        # Finished Menu
        message['text'] = "Calibration Finshed"
    elif(calibrationState == CalibrationState.FAILED):
        # Failed Menu
        message['text'] = "Calibration Failed"

# GUI Open Interrupt
def Open():
    global root
    root.pack()
    Update()

# GUI Close Interrupt
def Close():
    global root
    global calibrationState
    root.forget()
    calibrationState = CalibrationState.START

# Inputs
def InputInterrupt(interruptId):
    global calibrationState
    global apps1CurrentMin
    global apps1CurrentMax
    global apps2RawCurrentMin
    global apps2RawCurrentMax
    
    if(interruptId == 1):
        calibrationState = CalibrationState.START
    if(interruptId == 0):
        if(calibrationState == CalibrationState.START):
            calibrationState = CalibrationState.REQUEST_APPS_MIN

        elif(calibrationState == CalibrationState.REQUEST_APPS_MIN):
            apps1CurrentMin    = car_data.apps1
            apps2RawCurrentMin = car_data.apps2Raw
            calibrationState = CalibrationState.REQUEST_APPS_MAX

        elif(calibrationState == CalibrationState.REQUEST_APPS_MAX):
            apps1CurrentMax    = car_data.apps1
            apps2RawCurrentMax = car_data.apps2Raw
            ValidateCalibration()
            ApplyCalibration()
    Update()

def ValidateCalibration():
    global calibrationState
    global apps1CurrentMin
    global apps1CurrentMax
    global apps2RawCurrentMin
    global apps2RawCurrentMax

    # calibrationState = CalibrationState.FAILED
    # if(apps1CurrentMin    >= apps1CurrentMax):    return
    # if(apps2RawCurrentMin >= apps2RawCurrentMax): return
    calibrationState = CalibrationState.FINISHED

def ApplyCalibration():
    global calibrationState
    global apps1CurrentMin
    global apps1CurrentMax
    global apps2RawCurrentMin
    global apps2RawCurrentMax

    if(calibrationState != CalibrationState.FINISHED): return
    car_data.apps1Min    = apps1CurrentMin
    car_data.apps1Max    = apps1CurrentMax
    car_data.apps2RawMin = apps2RawCurrentMin
    car_data.apps2RawMax = apps2RawCurrentMax
    can.SendCommandAppsCalibration()