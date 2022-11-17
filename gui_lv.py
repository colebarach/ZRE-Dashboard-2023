# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

# Includes
import config
import car_data
import widgets

open = False

def Initialize(gui):
    global root
    global message

    root = widgets.CreateFrame(gui, grid=False)
    root.grid_columnconfigure(0, minsize=config.SCREEN_W)
    root.grid_rowconfigure(0,    minsize=config.SCREEN_H)
    message = widgets.CreateLabel(root, font=config.fontLarge)
    message.grid()

def Update():
    global open
    if(not open): return
    if(car_data.driveState == car_data.DriveState.INITIALIZING):
        message['text'] = "Booting..."
    elif(car_data.driveState == car_data.DriveState.LV_DRIVEOFF):
        message['text'] = "Low Voltage is on.\n\nWhen ready, have an ESO\nturn on high voltage."
    elif(car_data.driveState == car_data.DriveState.HV_DRIVEOFF):
        message['text'] = "High Voltage is on.\n\nPress and hold the brake,\nthen press the start button."

def Open():
    global open
    open = True
    root.pack()
    Update()

def Close():
    global open
    open = False
    root.forget()