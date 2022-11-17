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

# Themed Widgets ------------------------------------------------------------------------------------------
def ThemeFrame(parent, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.themeBackground, highlight=config.themeHighlight, border=False, borderWidth=config.themeBorderWidth, padding=config.themePadding):
    frame = Frame(parent, background=background)
    if(border):
        frame = Frame(parent, background=background, padx=padding, pady=padding, highlightbackground=highlight, highlightthickness=borderWidth)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame

def ThemeLabelFrame(parent, label, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.themeBackground, highlight=config.themeHighlight, fontColor=config.themeFontColor, font=config.themeFontMedium, border=False, borderWidth=config.themeBorderWidth, padding=config.themePadding):
    frame = LabelFrame(parent, text=label, background=background, foreground=fontColor, font=font)
    if(border):
        frame = LabelFrame(parent, text=label, background=background, padx=padding, pady=padding, highlightbackground=highlight, highlightthickness=borderWidth, font=font)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame

def ThemeCanvas(parent, width, height, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", backgroundColor=config.themeBackground, highlightColor=config.themeHighlight, border=False, borderWidth=config.themeBorderWidth):
    canvas = Canvas(parent, width=width, height=height, background=backgroundColor, highlightthickness=0)
    if(border):
        canvas = Canvas(parent, width=width, height=height, background=backgroundColor, highlightbackground=highlightColor, highlightthickness=borderWidth)
    if(grid):
        canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return canvas

def ThemeDividerHorizontal(parent, width, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", highlightColor=config.themeHighlight, borderWidth=config.themeBorderWidth):
    divider = Canvas(parent, width=width, height=borderWidth, background=highlightColor, highlightthickness=0)
    if(grid):
        divider.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return divider

def ThemeLabel(parent, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.themeBackground, fontColor=config.themeFontColor, font=config.themeFontMedium):
    label = Label(parent, font=font, text=text, foreground=fontColor, background=background)
    if(grid): label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return label

def ThemeButton(parent, command="", text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.themeBackground, fontColor=config.themeFontColor, font=config.themeFontMedium):
    button = Button(parent, command=command, text=text, font=font, foreground=fontColor, background=background)
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def ThemeProgressBar(parent, width, height, orientation, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.themeBackground, foreground=config.themeLowlight, highlight=config.themeHighlight, fontColor=config.themeFontColor, font=config.themeFontMedium, border=False, borderWidth=config.themeBorderWidth):
    bar = ProgressBar(parent, width, height, orientation, text=text, background=background, foreground=foreground, highlight=highlight, fontcolor=fontColor, font=font, border=border, borderWidth=borderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return bar

def ThemeButtonBar(parent, width, height, orientation, buttonCommands, buttonLabels=[""], grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.themeBackground, highlight=config.themeHighlight, fontColor=config.themeFontColor, font=config.themeFontMedium, border=False, borderWidth=config.themeBorderWidth):
    bar = ButtonBar(parent, width, height, orientation, buttonCommands, buttonLabels=buttonLabels, background=background, highlight=highlight, fontColor=fontColor, font=font, border=border, borderWidth=borderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

def ThemeStrataBar(parent, width, height, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", highlightPalette=[config.themeHighlight], lowlightPalette=[config.themeLowlight], paletteDomain=[1], strataSize=config.themeStrataSize, strataGap=config.themeStrataGap, strataSlope=config.themeStrataSlope, background=config.themeBackground, highlight=config.themeHighlight, fontColor=config.themeFontColor, font=config.themeFontMedium, border=False, borderWidth=config.themeBorderWidth, padding=config.themePadding, maskLeft=0, maskRight=0):
    mask = [0, height*maskLeft, width, 0, 0, height*maskRight]
    bar = StratifiedBar(parent, width, height, orientation, background=background, highlightPalette=highlightPalette, lowlightPalette=lowlightPalette, paletteDomain=paletteDomain, strataSize=strataSize, strataGap=strataGap, strataSlope=strataSlope, padx=padding, pady=padding, border=border, borderWidth=borderWidth, mask=mask)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return bar

def ThemeLabelStat(parent, value=None, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", highlightPalette=[config.themeFontColor], background=config.themeBackground, font=config.themeFontMedium):
    stat = LabelStat(parent, value=value, highlightPalette=highlightPalette, background=background, font=font)
    if(grid):
        stat.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return stat

# Plain Widgets -------------------------------------------------------------------------------------------
def PlainFrame(parent, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", border=False):
    frame = Frame(parent, background=config.plainBackground)
    if(border):
        frame = Frame(parent, background=config.plainBackground, padx=config.plainPadding, pady=config.plainPadding, highlightbackground=config.plainHighlight, highlightthickness=config.plainBorderWidth)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame

def PlainLabelFrame(parent, label, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    frame = LabelFrame(parent, text=label, background=config.plainBackground, padx=config.plainPadding, pady=config.plainPadding, foreground=config.plainFontColor, font=config.plainFontSmall)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame

def PlainLabel(parent, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    label = Label(parent, font=config.plainFontMedium, text=text, foreground=config.plainFontColor, background=config.plainBackground)
    if(grid): label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return label

def PlainButton(parent, command="", text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    button = Button(parent, command=command, text=text, font=config.plainFontSmall, foreground=config.plainFontColor, background=config.plainBackground)
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def PlainRadiobutton(parent, variable="", value=0, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    button = Radiobutton(parent, variable=variable, value=value, text=text, font=config.plainFontMedium, foreground=config.plainFontColor, background=config.plainBackground)
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def PlainEntry(parent, width, value="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    entry = Entry(parent, width=width, font=config.plainFontMedium, foreground=config.plainFontColor, bg=config.plainBackground)
    entry.insert(0,str(value))
    if(grid): entry.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return entry

def PlainCheckbutton(parent, variable, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    button = Checkbutton(parent, variable=variable, text=text, font=config.plainFontMedium, foreground=config.plainFontColor, background=config.plainBackground)
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def PlainDividerHorizontal(parent, width, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    divider = Canvas(parent, width=width, height=config.plainBorderWidth, background=config.plainHighlight, highlightthickness=0)
    if(grid):
        divider.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return divider

def PlainProgressBar(parent, width, height, orientation, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", foreground=config.plainHighlight, border=False):
    bar = ProgressBar(parent, width, height, orientation, text=text, background=config.plainBackground, foreground=foreground, highlight=config.plainHighlight, fontcolor=config.plainFontColor, font=config.plainFontMedium, border=border, borderWidth=config.plainBorderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return bar

def PlainButtonBar(parent, width, height, orientation, buttonCommands, buttonLabels=[""], grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", border=False):
    bar = ButtonBar(parent, width, height, orientation, buttonCommands, buttonLabels=buttonLabels, background=config.plainBackground, highlight=config.plainHighlight, fontColor=config.plainFontColor, font=config.plainFontMedium, border=border, borderWidth=config.plainBorderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

def PlainStrataBar(parent, width, height, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", border=False):
    bar = StratifiedBar(parent, width, height, orientation, background=config.plainBackground, highlightPalette=[config.plainBlue], lowlightPalette=[config.plainBackground], paletteDomain=[1], strataSize=config.plainStrataSize, strataGap=config.plainStrataGap, strataSlope=config.plainStrataSlope, padx=config.plainPadding, pady=config.plainPadding, border=True, borderWidth=config.plainBorderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return bar

def PlainLabelStat(parent, value=None, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", font=config.plainFontMedium):
    stat = LabelStat(parent, value=value, highlightPalette=[config.plainHighlight], background=config.plainBackground, font=font)
    if(grid):
        stat.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return stat

# Custom Widgets ------------------------------------------------------------------------------------------
class ProgressBar():
    def __init__(self, parent, width, height, orientation, value=None, text="", background='#F0F0F0', highlight='#AAAAAA', foreground='#444444', font=("consolas", 10), fontcolor="#000000", border=False, borderWidth=1):
        # Initialize Variables
        self.value       = value
        self.width       = width
        self.height      = height
        self.orientation = orientation
        self.text        = self.GetText(text)
        self.background  = background
        self.highlight   = highlight
        self.foreground  = foreground
        self.borderWidth = borderWidth
        self.font        = font
        self.fontcolor   = fontcolor
        # Create Canvas
        self.canvas = Canvas(parent, width=width, height=height, background=background, highlightthickness=0)
        if(border):
            self.borderWidth = 0
            canvasWidth  = width  - 2*borderWidth
            canvasHeight = height - 2*borderWidth
            self.canvas = Canvas(parent, width=canvasWidth, height=canvasHeight, background=background, highlightthickness=borderWidth, highlightbackground=highlight)
        self.Update()

    def GetText(self, text):
        if(self.orientation == "Horizontal"):
            return text
        if(self.orientation == "Vertical"):
            output = ""
            for index in range(len(text) - 1):
                output += text[index] + '\n'
            output += text[len(text)-1]
            return output
        return text

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def Update(self):
        if(self.value == None): return
        self.canvas.delete("Bar")
        self.canvas.delete("Text")
        barValue = 1 - self.value
        if(self.orientation == "Horizontal"):
            lowerCorner = (0, 0)
            upperCorner = (self.width * barValue, self.height)
        if(self.orientation == "Vertical"):
            lowerCorner = (0, self.height)
            upperCorner = (self.width, self.height * barValue)
        textPosition = (self.width/2, self.height/2)
        self.canvas.create_rectangle(lowerCorner[0], lowerCorner[1], upperCorner[0], upperCorner[1], width=0, fill=self.foreground, tags="Bar")
        self.canvas.create_text(textPosition[0], textPosition[1], text=self.text, font=self.font, fill=self.fontcolor, tags="Text")

    def Set(self, value, percent=False):
        if(percent):
            self.value = value / 100
        else:
            self.value = value
        self.Update()

    def Get(self):
        return self.value

class StratifiedBar():
    def __init__(self, parent, width, height, orientation, value=0, background='#F0F0F0', highlightPalette = ['#023399'], lowlightPalette = ['#F0F0F0'], paletteDomain = [1], strataSize = 8, strataGap = 2, strataSlope = 0, border=False, borderWidth = 1, borderColor='#AAAAAA', padx = 0, pady = 0, mask=[]):
        # Initialize Variables
        self.value           = value
        self.width           = width
        self.height          = height
        self.orientation     = orientation
        self.background      = background
        self.strataSize      = strataSize
        self.strataGap       = strataGap
        self.padx            = padx
        self.pady            = pady
        self.borderWidth     = borderWidth
        self.mask            = mask
        self.strataShear     = self.GetStrataShear(strataSlope)
        self.strataCount     = self.GetStrataCount()
        self.strataLowlights = self.GetStrataPalette(lowlightPalette,  paletteDomain)
        self.strataHighlight = self.GetStrataPalette(highlightPalette, paletteDomain)
        # Create Canvas
        self.canvas = Canvas(parent, width=width, height=height, bg=background, highlightthickness=0)
        if(border):
            self.canvas = Canvas(parent, width=width, height=height, bg=background, highlightbackground=borderColor, highlightthickness=borderWidth)
        self.Update()
    
    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

    def GetStrataShear(self, slope):
        if(self.orientation == "Horizontal"):
            return (self.height - 2*self.borderWidth - 2*self.pady) * slope
        if(self.orientation == "Vertical"):
            return (self.width  - 2*self.borderWidth - 2*self.padx) * slope
        return 0

    def GetStrataCount(self):
        if(self.orientation == "Horizontal"):
            return int((self.width  - 2*self.padx + 2*self.borderWidth - self.strataGap - self.strataShear) / (self.strataSize + self.strataGap))
        if(self.orientation == "Vertical"):
            return int((self.height - 2*self.pady + 2*self.borderWidth - self.strataGap - self.strataShear) / (self.strataSize + self.strataGap))

    def GetStrataPalette(self, palette, domain):
        strataPalette = []
        for strata in range(self.strataCount):
            for domainIndex in range(len(domain)):
                if(strata / self.strataCount < domain[domainIndex]):
                    strataPalette.append(palette[domainIndex])
                    break
        return strataPalette

    def Set(self, value, percent=False):
        if(percent):
            self.value = value / 100
        else:
            self.value = value
        self.Update()

    def Update(self):
        for strata in range(self.strataCount):
            self.RenderStrata(strata)
        self.RenderMask()
    
    def RenderStrata(self, index):
        strataName = "Strata" + str(index)
        self.canvas.delete(strataName)
        if(self.orientation == "Horizontal"):
            corner1 = (index * (self.strataSize + self.strataGap) + self.padx + self.borderWidth                   + self.strataShear, self.pady + self.borderWidth)
            corner2 = (index * (self.strataSize + self.strataGap) + self.strataSize + self.padx + self.borderWidth + self.strataShear, self.pady + self.borderWidth)
            corner3 = (index * (self.strataSize + self.strataGap) + self.strataSize + self.padx + self.borderWidth,                    self.height - self.pady + self.borderWidth)
            corner4 = (index * (self.strataSize + self.strataGap) + self.padx + self.borderWidth,                                      self.height - self.pady + self.borderWidth)
        if(self.orientation == "Vertical"):
            corner1 = (self.padx + self.borderWidth,              (self.strataCount - index) * (self.strataSize + self.strataGap) + self.pady + self.borderWidth                   + self.strataShear)
            corner2 = (self.padx + self.borderWidth,              (self.strataCount - index) * (self.strataSize + self.strataGap) + self.strataSize + self.pady + self.borderWidth + self.strataShear)
            corner3 = (self.width - self.padx + self.borderWidth, (self.strataCount - index) * (self.strataSize + self.strataGap) + self.strataSize + self.pady + self.borderWidth)
            corner4 = (self.width - self.padx + self.borderWidth, (self.strataCount - index) * (self.strataSize + self.strataGap) + self.pady + self.borderWidth)
        strataValue = index / self.strataCount
        if(strataValue < self.value):
            strataColor = self.strataHighlight[index]
        else:
            strataColor = self.strataLowlights[index]

        self.canvas.create_polygon(corner1[0], corner1[1], corner2[0], corner2[1], corner3[0], corner3[1], corner4[0], corner4[1], fill = strataColor, tags=strataName)

    def RenderMask(self):
        if(self.mask == []): return
        self.canvas.delete("Mask")
        self.canvas.create_polygon(*self.mask, fill=self.background)

class LabelStat():
    def __init__(self, parent, value=None, background='#F0F0F0', highlightPalette = ['#023399'], paletteDomain=[1], font=("consolas", 10)):
        self.label = Label(parent, font=font, bg=background)
        self.value = value
        self.highlightPalette = highlightPalette
        self.paletteDomain = paletteDomain
        self.Set(value)

    def Set(self, value):
        self.value = value
        self.Update()

    def Get(self):
        return self

    def Update(self):
        self.label['text'] = self.GetText()
        self.label['fg'] = self.GetColor()
        
    def GetText(self):
        if(self.value == None):
            return "--"
        return str(self.value)

    def GetColor(self):
        if(self.value == None): return self.highlightPalette[0]
        for index in range(len(self.paletteDomain)):
            if(self.value < self.paletteDomain[index]):
                return self.highlightPalette[index]
        return self.highlightPalette[len(self.highlightPalette) - 1]

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

class ButtonBar():
    def __init__(self, parent, width, height, orientation, buttonCommands, buttonLabels=[""], grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.plainBackground, highlight=config.plainHighlight, fontColor=config.plainFontColor, font=config.plainFontMedium, border=False, borderWidth=config.plainBorderWidth, padding=config.plainPadding):
        # Root Instantiation
        self.root = Frame(parent, background=background)
        if(border):
            self.root = Frame(parent, background=background, padx=padding, pady=padding, highlightbackground=highlight, highlightthickness=borderWidth)
        
        # Root Partitioning
        buttonCount = len(buttonCommands)
        if(orientation == "Horizontal"):
            self.root.rowconfigure(0, minsize=height)
            buttonWidth  = width / buttonCount
            buttonHeight = height
        if(orientation == "Vertical"):
            self.root.columnconfigure(0, minsize=width)
            buttonWidth  = width
            buttonHeight = height / buttonCount
        
        # Button Data
        buttons = numpy.empty(buttonCount, Button)
        if(buttonLabels == [""]):
            buttonLabels = numpy.empty(buttonCount,str)
        
        # Root Widgets
        for index in range(buttonCount):
            buttons[index] = Button(self.root, command=buttonCommands[index], text=buttonLabels[index], font=font, foreground=fontColor, background=background)
            if(orientation == "Horizontal"):
                self.root.columnconfigure(index, minsize=buttonWidth)
                buttons[index].grid(column=index, row=0, sticky="NESW")
            if(orientation == "Vertical"):
                self.root.rowconfigure(index, minsize=buttonHeight)
                buttons[index].grid(column=0, row=index, sticky="NESW")

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.root.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)