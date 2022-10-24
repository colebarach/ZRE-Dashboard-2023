# Title: GUI Widget Library
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: Collection of functions and objects for the GUI. Create all display widgets using this module, rather than directly though
#   TKinter, as this provides a frontend for managing style and consistency.

# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

import numpy
import math

# Includes
import config

def CreateFrame(parent, border=False, grid=True, column=0, row=0, backgroundColor=config.backgroundColor, highlightColor=config.highlightColor, borderWidth=config.borderWidth, padding=config.padding, columnspan=1, rowspan=1, sticky=""):
    frame = Frame(parent, background=backgroundColor)
    if(border):
        frame = Frame(parent, background=backgroundColor, padx=padding, pady=padding, highlightbackground=highlightColor, highlightthickness=borderWidth)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame
        
def CreateCanvas(parent, width, height, border=False, grid=True, column=0, row=0, backgroundColor=config.backgroundColor, highlightColor=config.highlightColor, borderWidth=config.borderWidth, columnspan=1, rowspan=1, sticky=""):
    canvas = Canvas(parent, width=width, height=height, background=backgroundColor, highlightthickness=0)
    if(border):
        canvas = Canvas(parent, width=width, height=height, background=backgroundColor, highlightbackground=highlightColor, highlightthickness=borderWidth)
    if(grid):
        canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return canvas

def CreateDividerHorizontal(parent, width, grid=True, column=0, row=0, highlightColor=config.highlightColor, borderWidth=config.borderWidth, columnspan=1, rowspan=1):
    divider = Canvas(parent, width=width, height=borderWidth, background=highlightColor, highlightthickness=0)
    if(grid):
        divider.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan)
    return divider

def CreateLabel(parent, text="", grid=False, column=0, row=0, font=config.font, fontColor=config.fontColor, background=config.backgroundColor, sticky=""):
    label = Label(parent, font=font, text=text, foreground=fontColor, background=background)
    if(grid): label.grid(column=column, row=row, sticky=sticky)
    return label

def CreateButton(parent, command="", text="", grid=False, column=0, row=0, sticky="", font=config.font, fontColor=config.fontColor, background=config.backgroundColor):
    button = Button(parent, command=command, text=text, font=font, foreground=fontColor, background=background)
    if(grid): button.grid(column=column, row=row, sticky=sticky)
    return button

class LabelBarHorizontal():
    def __init__(self, parent, width, height, labelNames=[""], border=False, column=0, row=0, backgroundColor=config.backgroundColor, highlightColor=config.highlightColor, borderWidth=config.borderWidth, fontColor=config.fontColor, font=config.font, padding=0, columnspan=1, rowspan=1):
        self.root = CreateFrame(parent, border=border, grid=True, column=column, row=row, backgroundColor=backgroundColor, highlightColor=highlightColor, borderWidth=borderWidth, padding=padding, columnspan=columnspan, rowspan=rowspan)
        self.root.rowconfigure(0, minsize=height)
        self.root.grid(column=column, row=row)
        labelCount = len(labelNames)
        labelWidth = width/labelCount
        labels = numpy.empty(labelCount, Label)
        for index in range(labelCount):
            self.root.columnconfigure(index, minsize=labelWidth)
            labels[index] = CreateLabel(self.root, text=labelNames[index], grid=True, column=index, row=0, font=font, fontColor=fontColor, background=backgroundColor)

class ProgressBarVertical():
    def __init__(self, parent, width, height, column=0, row=0, text="", border=False, backgroundcolor=config.backgroundColor, highlightColor=config.highlightColor, lowlightColor=config.lowlightColor, borderWidth=config.borderWidth, font=config.font, fontcolor=config.fontColor, columnspan=1, rowspan=1, sticky=""):
        # Initialize Variables
        self.width           = width
        self.height          = height
        self.text            = text
        self.backgroundColor = backgroundcolor
        self.highlightColor  = highlightColor
        self.lowlightColor   = lowlightColor
        self.borderWidth     = borderWidth
        self.font            = font
        self.fontcolor       = fontcolor
        # Create Canvas
        self.canvas = CreateCanvas(parent, width - borderWidth*2, height - borderWidth*2, border=border, column=column, row=row, backgroundColor=backgroundcolor, highlightColor=highlightColor, borderWidth=borderWidth, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
        self.SetBar(0)
    
    def SetBar(self,value):
        self.canvas.delete("bar")
        self.canvas.delete("title")
        self.canvas.create_rectangle(0, self.height, self.width + config.borderWidth*2, self.height*(1-value), width=0, fill=self.lowlightColor, tags="bar")
        self.canvas.create_text(self.width/2,self.height/2, text=self.text, font=self.font, fill=self.fontcolor, tags="title")

class ProgressBarHorizontal():
    def __init__(self, parent, width, height, column=0, row=0, text="", border=False, backgroundcolor=config.backgroundColor, highlightColor=config.highlightColor, lowlightColor=config.lowlightColor, borderWidth=config.borderWidth, font=config.font, fontcolor=config.fontColor, columnspan=1, rowspan=1, sticky=""):
        # Initialize Variables
        self.width           = width
        self.height          = height
        self.text            = text
        self.backgroundColor = backgroundcolor
        self.highlightColor  = highlightColor
        self.lowlightColor   = lowlightColor
        self.borderWidth     = borderWidth
        self.font            = font
        self.fontcolor       = fontcolor
        # Create Canvas
        self.canvas = CreateCanvas(parent, width - borderWidth*2, height - borderWidth*2, border=border, column=column, row=row, backgroundColor=backgroundcolor, highlightColor=highlightColor, borderWidth=borderWidth, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
        self.SetBar(0)
    
    def SetBar(self,value):
        self.canvas.delete("bar")
        self.canvas.delete("title")
        self.canvas.create_rectangle(0, 0, self.width*value, self.height + config.borderWidth*2, width=0, fill=self.lowlightColor, tags="bar")
        self.canvas.create_text(self.width/2,self.height/2, text=self.text, font=self.font, fill=self.fontcolor, tags="title")

class ButtonBarHorizontal():
    def __init__(self, parent, width, height, buttonCommands, buttonNames=[""], border=False, column=0, row=0, backgroundColor=config.backgroundColor, highlightColor=config.highlightColor, borderWidth=config.borderWidth, fontColor=config.fontColor, font=config.font, padding=0, columnspan=1, rowspan=1):
        self.root = CreateFrame(parent, border=border, grid=True, column=column, row=row, backgroundColor=backgroundColor, highlightColor=highlightColor, borderWidth=borderWidth, padding=padding, columnspan=columnspan, rowspan=rowspan)
        self.root.rowconfigure(0, minsize=height)
        self.root.grid(column=column, row=row)
        buttonCount = len(buttonCommands)
        buttonWidth = width/buttonCount
        buttons = numpy.empty(buttonCount, Button)
        for index in range(buttonCount):
            self.root.columnconfigure(index, minsize=buttonWidth)
            buttons[index] = CreateButton(self.root, command=buttonCommands[index], text=buttonNames[index], grid=True, column=index, row=0, sticky="NESW", font=font, fontColor=fontColor, background=backgroundColor)

class StratifiedBarHorizontal():
    def __init__(self, parent, width, height, column=0, row=0, backgroundcolor=config.backgroundColor, rangeColorsLow = [config.lowlightColor], rangeColorsHigh = [config.highlightColor], rangeValues = [1], columnspan=1, rowspan=1, strataWidth = config.strataWidth, strataShear = config.strataShear, maskLeft = -1, maskRight = -1):
        # Initialize Variables
        self.width            = width
        self.height           = height
        self.backgroundColor  = backgroundcolor
        self.strataWidth      = strataWidth
        self.strataShear      = strataShear
        self.maskLeft         = maskLeft
        self.maskRight        = maskRight
        self.strataCount      = math.floor(((width - strataShear) / (strataWidth * 2)))
        self.strataColorsLow  = self.GetStrataColors(rangeColorsLow,  rangeValues)
        self.strataColorsHigh = self.GetStrataColors(rangeColorsHigh, rangeValues)
        # Create Canvas
        self.canvas = CreateCanvas(parent, width, height, border=False, column=column, row=row, backgroundColor=backgroundcolor, columnspan=columnspan, rowspan=rowspan)
        self.SetBar(0)
    
    def SetBar(self, value):
        for strata in range(self.strataCount):
            self.canvas.delete("strata" + str(strata))
            xPosition = (strata * 2 + 1) * self.strataWidth
            strataValue = strata / self.strataCount
            strataColor = self.strataColorsLow[strata]
            if(strataValue < value):
                strataColor = self.strataColorsHigh[strata]
            self.canvas.create_polygon(xPosition + self.strataShear, 0, xPosition + self.strataWidth + self.strataShear, 0, xPosition + self.strataWidth, self.height, xPosition, self.height, fill = strataColor, tags="strata" + str(strata))
        if(self.maskRight >= 0 and self.maskLeft >= 0):
            self.canvas.delete("mask")
            self.canvas.create_polygon(0, 0, 0, self.maskLeft, self.width, self.maskRight, self.width, 0, fill=self.backgroundColor, tags="mask")
    
    def GetStrataColors(self, colorRanges, rangeValues):
        strataColors = []
        for strata in range(self.strataCount):
            for rangeIndex in range(len(rangeValues)):
                if(strata / self.strataCount < rangeValues[rangeIndex]):
                    strataColors.append(colorRanges[rangeIndex])
                    break
        return strataColors