# Title: GUI Debug
# Author: Cole Barach
# Date Created: 22.11.07
# Date Updated: 22.11.07
# Function: GUI Debug Script. Frontend file for testing CAN messages.

# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

import enum
from enum import Enum

# Includes
import can
import widgets
import config
import car_data

def Initialize(guiRoot):
    # Root Declaration & Window Instantiation
    global root
    root = Toplevel(guiRoot)
    root.title("Dashboard 2023 - Debug Module")
    root.resizable(0, 0)
    # Root Partitioning
    column0Width = 280
    column1Width = config.debugGuiWidth - column0Width
    root.columnconfigure(0, minsize=column0Width)
    root.columnconfigure(1, minsize=column1Width)
    # Panel Instantiations
    inputPedalsRoot            = widgets.PlainLabelFrame(root, label="Input Pedals: 0x005",             sticky="NESW", column=0, row=0)
    dataMotorRoot              = widgets.PlainLabelFrame(root, label="Data Motor: 0x0A7",               sticky="NESW", column=0, row=1)
    commandAppsCalibrationRoot = widgets.PlainLabelFrame(root, label="Command APPS Calibration: 0x533", sticky="NESW", column=0, row=2)
    dataPedalsRoot             = widgets.PlainLabelFrame(root, label="Data Pedals: 0x701",              sticky="NESW", column=0, row=3)
    statusEcuRoot              = widgets.PlainLabelFrame(root, label="Status ECU: 0x703",               sticky="NESW", column=1, row=0, rowspan=4)
    # Initializations
    InitializeInputPedals           (inputPedalsRoot,            column0Width)
    InitializeDataMotor             (dataMotorRoot,              column0Width)
    InitializeCommandAppsCalibration(commandAppsCalibrationRoot, column0Width)
    InitializeDataPedals            (dataPedalsRoot,             column0Width)
    InitializeStatusEcu             (statusEcuRoot,              column1Width)

def InitializeInputPedals(inputPedalsRoot, width):
    # Input Parameters
    global apps1Input
    global apps2Input
    global brake1Input
    global brake2Input
    # Partitioning
    buttonWidth = 40
    labelWidth = 180
    inputWidth = width - buttonWidth - labelWidth
    inputPedalsRoot.columnconfigure(0, minsize=labelWidth)
    inputPedalsRoot.columnconfigure(1, minsize=inputWidth)
    inputPedalsRoot.columnconfigure(2, minsize=buttonWidth)
    # Send Button
    widgets.PlainButton(inputPedalsRoot, text="Send", command=SendInputPedals, column=2, row=0, sticky="E")
    # Labels
    widgets.PlainLabel(inputPedalsRoot, text="APPS-1 Value",  column=0, row=0, sticky="W")
    widgets.PlainLabel(inputPedalsRoot, text="APPS-2 Value",  column=0, row=1, sticky="W")
    widgets.PlainLabel(inputPedalsRoot, text="Brake-1 Value", column=0, row=2, sticky="W")
    widgets.PlainLabel(inputPedalsRoot, text="Brake-2 Value", column=0, row=3, sticky="W")
    # Inputs
    apps1Input  = widgets.PlainEntry(inputPedalsRoot, width=8, value=0, column=1, row=0, sticky="E")
    apps2Input  = widgets.PlainEntry(inputPedalsRoot, width=8, value=0, column=1, row=1, sticky="E")
    brake1Input = widgets.PlainEntry(inputPedalsRoot, width=8, value=0, column=1, row=2, sticky="E")
    brake2Input = widgets.PlainEntry(inputPedalsRoot, width=8, value=0, column=1, row=3, sticky="E")
    
def InitializeDataMotor(dataMotorRoot, width):
    # Input Parameters
    global motorAngleInput
    global motorRpmInput
    global motorFrequencyInput
    global motorDeltaResolverInput
    # Partitioning
    buttonWidth = 40
    labelWidth = 180
    inputWidth = width - buttonWidth - labelWidth
    dataMotorRoot.columnconfigure(0, minsize=labelWidth)
    dataMotorRoot.columnconfigure(1, minsize=inputWidth)
    dataMotorRoot.columnconfigure(2, minsize=buttonWidth)
    # Send Button
    widgets.PlainButton(dataMotorRoot, text="Send", command=SendDataMotor, column=2, row=0, sticky="E")
    # Labels
    widgets.PlainLabel(dataMotorRoot, text="Motor Angle",          column=0, row=0, sticky="W")
    widgets.PlainLabel(dataMotorRoot, text="Motor RPM",            column=0, row=1, sticky="W")
    widgets.PlainLabel(dataMotorRoot, text="Motor Frequency",      column=0, row=2, sticky="W")
    widgets.PlainLabel(dataMotorRoot, text="Motor Delta Resolver", column=0, row=3, sticky="W")
    # Inputs
    motorAngleInput         = widgets.PlainEntry(dataMotorRoot, width=8, column=1, row=0, value=0, sticky="E")
    motorRpmInput           = widgets.PlainEntry(dataMotorRoot, width=8, column=1, row=1, value=0, sticky="E")
    motorFrequencyInput     = widgets.PlainEntry(dataMotorRoot, width=8, column=1, row=2, value=0, sticky="E")
    motorDeltaResolverInput = widgets.PlainEntry(dataMotorRoot, width=8, column=1, row=3, value=0, sticky="E")

def InitializeCommandAppsCalibration(commandAppsCalibrationRoot, width):
    # Input Parameters
    global apps1MinInput
    global apps1MaxInput
    global apps2MinInput
    global apps2MaxInput
    # Partitioning
    buttonWidth = 40
    labelWidth = 180
    inputWidth = width - buttonWidth - labelWidth
    commandAppsCalibrationRoot.columnconfigure(0, minsize=labelWidth)
    commandAppsCalibrationRoot.columnconfigure(1, minsize=inputWidth)
    commandAppsCalibrationRoot.columnconfigure(2, minsize=buttonWidth)
    # Send Button
    widgets.PlainButton(commandAppsCalibrationRoot, text="Send", command=SendCommandAppsCalibration, column=2, row=0, sticky="E")
    # Labels
    widgets.PlainLabel(commandAppsCalibrationRoot, text="APPS-1 Min", column=0, row=0, sticky="W")
    widgets.PlainLabel(commandAppsCalibrationRoot, text="APPS-1 Max", column=0, row=1, sticky="W")
    widgets.PlainLabel(commandAppsCalibrationRoot, text="APPS-2 Min", column=0, row=2, sticky="W")
    widgets.PlainLabel(commandAppsCalibrationRoot, text="APPS-2 Max", column=0, row=3, sticky="W")
    # Inputs
    apps1MinInput = widgets.PlainEntry(commandAppsCalibrationRoot, width=8, column=1, row=0, value=0, sticky="E")
    apps1MaxInput = widgets.PlainEntry(commandAppsCalibrationRoot, width=8, column=1, row=1, value=0, sticky="E")
    apps2MinInput = widgets.PlainEntry(commandAppsCalibrationRoot, width=8, column=1, row=2, value=0, sticky="E")
    apps2MaxInput = widgets.PlainEntry(commandAppsCalibrationRoot, width=8, column=1, row=3, value=0, sticky="E")

def InitializeDataPedals(dataPedalsRoot, width):
    # Input Parameters
    global apps1PercentInput
    global apps2PercentInput
    global brake1PercentInput
    global brake2PercentInput
    # Partitioning
    buttonWidth = 40
    labelWidth = 180
    inputWidth = width - buttonWidth - labelWidth
    dataPedalsRoot.columnconfigure(0, minsize=labelWidth)
    dataPedalsRoot.columnconfigure(1, minsize=inputWidth)
    dataPedalsRoot.columnconfigure(2, minsize=buttonWidth)
    # Send Button
    widgets.PlainButton(dataPedalsRoot, text="Send", command=SendDataPedals, column=2, row=0, sticky="E")
    # Labels
    widgets.PlainLabel(dataPedalsRoot, text="APPS-1 Percent",  column=0, row=0, sticky="W")
    widgets.PlainLabel(dataPedalsRoot, text="APPS-2 Percent",  column=0, row=1, sticky="W")
    widgets.PlainLabel(dataPedalsRoot, text="Brake-1 Percent", column=0, row=2, sticky="W")
    widgets.PlainLabel(dataPedalsRoot, text="Brake-2 Percent", column=0, row=3, sticky="W")
    # Inputs
    apps1PercentInput  = widgets.PlainEntry(dataPedalsRoot, width=8, column=1, row=0, value=0, sticky="E")
    apps2PercentInput  = widgets.PlainEntry(dataPedalsRoot, width=8, column=1, row=1, value=0, sticky="E")
    brake1PercentInput = widgets.PlainEntry(dataPedalsRoot, width=8, column=1, row=2, value=0, sticky="E")
    brake2PercentInput = widgets.PlainEntry(dataPedalsRoot, width=8, column=1, row=3, value=0, sticky="E")
  
def InitializeStatusEcu(statusEcuRoot, width):
    # Input Parameters
    global driveStateInput
    global acceleratingInput
    global brakingInput
    global drsInput
    global regenInput
    global is25_5Input
    global inverterInput
    global acanInput
    global is100msInput
    global torquePercentInput
    global regenPercentInput
    global voltageLvInput
    global resistanceImdInput
    # Partitioning
    buttonWidth = 40
    labelWidth = 165
    inputWidth = width - buttonWidth - labelWidth
    statusEcuRoot.columnconfigure(0, minsize=labelWidth)
    statusEcuRoot.columnconfigure(1, minsize=inputWidth)
    statusEcuRoot.columnconfigure(2, minsize=buttonWidth)
    # Send Button
    widgets.PlainButton(statusEcuRoot, text="Send", command=SendStatusEcu, column=2, row=0, sticky="E")
    # Labels
    widgets.PlainLabel(statusEcuRoot, text="Drive State",           column=0, row=0,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="Is Accelerating",       column=0, row=1,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="Is Braking",            column=0, row=2,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="DRS Enabled",           column=0, row=3,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="Regen Enabled",         column=0, row=4,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="25/5 Implausible",      column=0, row=5,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="Inverter Fault",        column=0, row=6,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="ACAN Implausible",      column=0, row=7,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="100ms Implausible",     column=0, row=8,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="Torque Percentage Max", column=0, row=9,  sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="Regen Percentage Max",  column=0, row=10, sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="LV Battery Voltage",    column=0, row=11, sticky="W")
    widgets.PlainLabel(statusEcuRoot, text="IMD Resistance",        column=0, row=12, sticky="W")
    # Inputs
    driveStateInput   = IntVar(value=0)
    acceleratingInput = BooleanVar(value=False)
    brakingInput      = BooleanVar(value=False)
    drsInput          = BooleanVar(value=False)
    regenInput        = BooleanVar(value=False)
    is25_5Input       = BooleanVar(value=False)
    inverterInput     = BooleanVar(value=False)
    acanInput         = BooleanVar(value=False)
    is100msInput      = BooleanVar(value=False)
    # Selection Inputs
    driveStateFrame = widgets.PlainFrame(statusEcuRoot, column=1, row=0)
    widgets.PlainRadiobutton(driveStateFrame, variable=driveStateInput, text="Initializing", value=0, column=0,row=0, sticky="W")
    widgets.PlainRadiobutton(driveStateFrame, variable=driveStateInput, text="LV Drive OFF", value=1, column=0,row=1, sticky="W")
    widgets.PlainRadiobutton(driveStateFrame, variable=driveStateInput, text="HV Drive OFF", value=2, column=0,row=2, sticky="W")
    widgets.PlainRadiobutton(driveStateFrame, variable=driveStateInput, text="HV Drive ON",  value=3, column=0,row=3, sticky="W")
    # Boolean Inputs
    widgets.PlainCheckbutton(statusEcuRoot, acceleratingInput, column=1, row=1, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, brakingInput,      column=1, row=2, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, drsInput,          column=1, row=3, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, regenInput,        column=1, row=4, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, is25_5Input,       column=1, row=5, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, inverterInput,     column=1, row=6, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, acanInput,         column=1, row=7, sticky="W")
    widgets.PlainCheckbutton(statusEcuRoot, is100msInput,      column=1, row=8, sticky="W")
    # Numeric Inputs
    torquePercentInput = widgets.PlainEntry(statusEcuRoot, width=16, column=1, row=9,  value=0, sticky="E")
    regenPercentInput  = widgets.PlainEntry(statusEcuRoot, width=16, column=1, row=10, value=0, sticky="E")
    voltageLvInput     = widgets.PlainEntry(statusEcuRoot, width=16, column=1, row=11, value=0, sticky="E")
    resistanceImdInput = widgets.PlainEntry(statusEcuRoot, width=16, column=1, row=12, value=0, sticky="E")

def SendInputPedals():
    global apps1Input
    global apps2Input
    global brake1Input
    global brake2Input
    apps1  = int(apps1Input.get())
    apps2  = int(apps2Input.get())
    brake1 = int(brake1Input.get())
    brake2 = int(brake2Input.get())
    can.SendInputPedals(apps1, apps2, brake1, brake2)

def SendDataMotor():
    global motorAngleInput
    global motorRpmInput
    global motorFrequencyInput
    global motorDeltaResolverInput
    motorAngle         = int(motorAngleInput.get())
    motorRpm           = int(motorRpmInput.get())
    motorFrequency     = int(motorFrequencyInput.get())
    motorDeltaResolver = int(motorDeltaResolverInput.get())
    can.SendDataMotor(motorAngle, motorRpm, motorFrequency, motorDeltaResolver)

def SendCommandAppsCalibration():
    global apps1MinInput
    global apps1MaxInput
    global apps2MinInput
    global apps1MaxInput
    apps1MinValue = int(apps1MinInput.get())
    apps1MaxValue = int(apps1MaxInput.get())
    apps2MinValue = int(apps2MinInput.get())
    apps2MaxValue = int(apps2MaxInput.get())
    can.SendCommandAppsCalibration(apps1MinValue, apps1MaxValue, apps2MinValue, apps2MaxValue)

def SendDataPedals():
    global apps1PercentInput
    global apps2PercentInput
    global brake1PercentInput
    global brake2PercentInput
    apps1Percent  = int(apps1PercentInput.get())
    apps2Percent  = int(apps2PercentInput.get())
    brake1Percent = int(brake1PercentInput.get())
    brake2Percent = int(brake2PercentInput.get())
    can.SendDataPedals(apps1Percent, apps2Percent, brake1Percent, brake2Percent)

def SendStatusEcu():
    global driveStateInput
    global acceleratingInput
    global brakingInput
    global drsInput
    global regenInput
    global is25_5Input
    global inverterInput
    global acanInput
    global is100msInput
    global torquePercentInput
    global regenPercentInput
    global voltageLvInput
    global resistanceImdInput
    driveStateValue    = int(driveStateInput.get())
    acceleratingValue  = acceleratingInput.get()
    brakingValue       = brakingInput.get()
    drsValue           = drsInput.get()
    regenValue         = regenInput.get()
    is25_5Value        = is25_5Input.get()
    inverterValue      = inverterInput.get()
    acanValue          = acanInput.get()
    is100msValue       = is100msInput.get()
    torquePercentValue = int(torquePercentInput.get())
    regenPercentValue  = int(regenPercentInput.get())
    voltageLvValue     = float(voltageLvInput.get())
    resistanceImdValue = float(resistanceImdInput.get())
    can.SendStatusEcu(driveStateValue, acceleratingValue, brakingValue, drsValue, regenValue, is25_5Value, inverterValue, acanValue, is100msValue, torquePercentValue, regenPercentValue, voltageLvValue, resistanceImdValue)