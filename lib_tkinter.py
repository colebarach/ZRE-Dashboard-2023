# Title: Tkinter Library Interface
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.11.29
# Function: Frontend for the Standard TKinter Library. Provides a collection of functions and objects that are consistent in stylization.
#   and behavior. All TKinter usage should be managed using this module, rather than directly.

# Libraries
import tkinter
from tkinter            import *
from tkinter            import font

import numpy

# Includes
import config

# Dash Widgets ----------------------------------------------------------------------------------------------------------------------------------------------------
def DashFrame(parent, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, highlight=config.dashHighlight, border=False, borderWidth=config.dashBorderWidth, padding=config.dashPadding):
    frame = Frame(parent, background=background)
    if(border):
        frame = Frame(parent, background=background, padx=padding, pady=padding, highlightbackground=highlight, highlightthickness=borderWidth)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame

def DashLabelFrame(parent, label, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, fontColor=config.dashFontColor, font=config.dashFontExtraSmall, border=False, borderWidth=config.dashBorderWidth, padding=config.dashPadding):
    frame = LabelFrame(parent, text=label, bg=background, fg=fontColor, font=font)
    if(border):
        frame = LabelFrame(parent, text=label, bg=background, fg=fontColor, font=font, padx=padding, pady=padding, bd=borderWidth)        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return frame

def DashCanvas(parent, width, height, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", backgroundColor=config.dashBackground, highlightColor=config.dashHighlight, border=False, borderWidth=config.dashBorderWidth):
    canvas = Canvas(parent, width=width, height=height, background=backgroundColor, highlightthickness=0)
    if(border):
        canvas = Canvas(parent, width=width, height=height, background=backgroundColor, highlightbackground=highlightColor, highlightthickness=borderWidth)
    if(grid):
        canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return canvas

def DashDivider(parent, size, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", highlightColor=config.dashHighlight, borderWidth=config.dashBorderWidth):
    if(orientation == "Horizontal"):
        divider = Canvas(parent, width=size, height=borderWidth, background=highlightColor, highlightthickness=0)
    if(orientation == "Vertical"):
        divider = Canvas(parent, width=borderWidth, height=size, background=highlightColor, highlightthickness=0)
    if(grid):
        divider.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return divider

def DashLabel(parent, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, fontColor=config.dashFontColor, font=config.dashFontMedium):
    label = Label(parent, font=font, text=text, foreground=fontColor, background=background)
    if(grid): label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return label

def DashButton(parent, command="", text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, fontColor=config.dashFontColor, font=config.dashFontMedium):
    button = Button(parent, command=command, text=text, font=font, foreground=fontColor, background=background)
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def DashProgressBar(parent, width, height, orientation, value=0, scaleFactor=1, offset=0, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, foreground=config.dashLowlight, highlight=config.dashHighlight, fontColor=config.dashFontColor, font=config.dashFontMedium, border=False, borderWidth=config.dashBorderWidth):
    bar = ProgressBar(parent, width, height, orientation, value=value, scaleFactor=scaleFactor, offset=offset, text=text, background=background, foreground=foreground, highlight=highlight, fontcolor=fontColor, font=font, border=border, borderWidth=borderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return bar

def DashButtonBar(parent, width, height, orientation, buttonCommands, buttonLabels=[""], grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, highlight=config.dashHighlight, fontColor=config.dashFontColor, font=config.dashFontMedium, border=False, borderWidth=config.dashBorderWidth):
    bar = ButtonBar(parent, width, height, orientation, buttonCommands, buttonLabels=buttonLabels, background=background, highlight=highlight, fontColor=fontColor, font=font, border=border, borderWidth=borderWidth)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

def DashStrataBar(parent, width, height, orientation, scaleFactor=1, offset=0, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", highlightPalette=[config.dashHighlight], lowlightPalette=[config.dashLowlight], paletteDomain=[1], strataSize=config.dashStrataSize, strataGap=config.dashStrataGap, strataSlope=config.dashStrataSlope, background=config.dashBackground, highlight=config.dashHighlight, fontColor=config.dashFontColor, font=config.dashFontMedium, border=False, borderWidth=config.dashBorderWidth, padding=config.dashPadding, maskLeft=0, maskRight=0):
    mask = [0, 0, 0, height*maskLeft, width, height*maskRight, width, 0]
    bar = StratifiedBar(parent, width, height, orientation, scaleFactor=scaleFactor, offset=offset, background=background, highlightPalette=highlightPalette, lowlightPalette=lowlightPalette, paletteDomain=paletteDomain, strataSize=strataSize, strataGap=strataGap, strataSlope=strataSlope, padx=padding, pady=padding, border=border, borderWidth=borderWidth, mask=mask)
    if(grid):
        bar.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return bar

def DashLabelStat(parent, value=None, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", paletteDomain=[1], highlightPalette=[config.dashFontColor], backgroundPalette=[config.dashBackground], font=config.dashFontMedium):
    stat = LabelStat(parent, value=value, paletteDomain=paletteDomain, highlightPalette=highlightPalette, backgroundPalette=backgroundPalette, font=font)
    if(grid):
        stat.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return stat

def DashLabelCanvas(parent, width, height, xPosition, yPosition, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.dashBackground, font=config.dashFontMedium, fontColor=config.dashFontColor):
    canvas = Canvas(parent, width=width, height=height, background=background, highlightthickness=0)
    if(grid):
        canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    canvas.create_text(xPosition, yPosition, text=text, fill=fontColor, font=font)
    return canvas

def DashBmsCellStat(parent, width, height, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", voltageError=config.voltageErrorColor, balancePalette=config.balancingPalette, temperaturePalette=config.tempPalette, voltageDomain=config.voltageRange, temperatureDomain=config.tempDomain, fontColor=config.dashFontColor, font=config.dashFontBareSmall, borderWidth=3):
    stat = BmsCellStat(parent, width, height, voltageError=voltageError, balancePalette=balancePalette, temperaturePalette=temperaturePalette, voltageDomain=voltageDomain, temperatureDomain=temperatureDomain, fontColor=fontColor, font=font, borderWidth=borderWidth)
    if(grid):
        stat.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return stat

def DashCheckStat(parent, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", inverted=False, background=config.dashBackground, foreground=config.dashFontColor, font=config.dashFontMedium):
    stat = CheckStat(parent, inverted=inverted, foreground=foreground, background=background, font=font)
    if(grid):
        stat.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return stat

# Plain Widgets ---------------------------------------------------------------------------------------------------------------------------------------------------
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
    stat = LabelStat(parent, value=value, highlightPalette=[config.plainHighlight], backgroundPalette=[config.plainBackground], font=font)
    if(grid):
        stat.Grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return stat

# Custom Widgets --------------------------------------------------------------------------------------------------------------------------------------------------
class ProgressBar():
    def __init__(self, parent, width, height, orientation, value=None, scaleFactor=1, offset=0, text="", background='#F0F0F0', highlight='#AAAAAA', foreground='#444444', font=("consolas", 10), fontcolor="#000000", border=False, borderWidth=1):
        # Initialize Variables
        self.value       = value
        self.scaleFactor = scaleFactor
        self.offset      = offset
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
        self.InitializeBar()
        self.InitializeText()
        self.Update()

    def GetText(self, text):
        if(len(text) < 2): return text
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

    def InitializeText(self):
        textPosition = (self.width/2, self.height/2)
        self.canvas.create_text(textPosition[0], textPosition[1], text=self.text, font=self.font, fill=self.fontcolor, tags="Text")

    def InitializeBar(self):
        self.canvas.create_rectangle(0, 0, 0, 0, width=0, fill=self.foreground, tags="Bar")

    def Update(self):
        if(self.value == None): return
        if(self.orientation == "Horizontal"):
            lowerCorner = (0, 0)
            upperCorner = (self.width * (self.value-self.offset) / self.scaleFactor, self.height)
        if(self.orientation == "Vertical"):
            lowerCorner = (0, self.height)
            upperCorner = (self.width, self.height * (1 - (self.value-self.offset) / self.scaleFactor))
        self.canvas.coords("Bar", lowerCorner[0], lowerCorner[1], upperCorner[0], upperCorner[1])

    def Set(self, value):
        if(value == None): return
        self.value = value
        self.Update()

    def Get(self):
        return self.value

class StratifiedBar():
    def __init__(self, parent, width, height, orientation, value=None, scaleFactor=1, offset=0, background='#F0F0F0', highlightPalette = ['#023399'], lowlightPalette = ['#F0F0F0'], paletteDomain = [1], strataSize = 8, strataGap = 2, strataSlope = 0, border=False, borderWidth = 1, borderColor='#AAAAAA', padx = 0, pady = 0, mask=[]):
        # Initialize Variables
        self.value            = value
        self.scaleFactor      = scaleFactor
        self.offset           = offset
        self.width            = width
        self.height           = height
        self.orientation      = orientation
        self.background       = background
        self.strataSize       = strataSize
        self.strataGap        = strataGap
        self.padx             = padx
        self.pady             = pady
        self.borderWidth      = borderWidth
        self.mask             = mask
        self.strataShear      = self.GetStrataShear(strataSlope)
        self.strataCount      = self.GetStrataCount()
        self.strataLowlights  = self.GetStrataPalette(lowlightPalette,  paletteDomain)
        self.strataHighlights = self.GetStrataPalette(highlightPalette, paletteDomain)
        # Create Canvas
        self.canvas = Canvas(parent, width=width, height=height, bg=background, highlightthickness=0)
        if(border):
            self.canvas = Canvas(parent, width=width, height=height, bg=background, highlightbackground=borderColor, highlightthickness=borderWidth)
        for strata in range(self.strataCount):
            self.InitializeStrata(strata)
        self.InitializeMask()
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
                if(strata / self.strataCount < (domain[domainIndex]-self.offset) / self.scaleFactor):
                    strataPalette.append(palette[domainIndex])
                    break
        return strataPalette

    def Set(self, value, percent=False):
        if(value == None): return
        if(percent):
            self.value = value / 100
        else:
            self.value = value
        self.Update()

    def Update(self):
        if(self.value == None): return
        for strata in range(self.strataCount):
            self.UpdateStrata(strata)
    
    def InitializeStrata(self, index):
        strataName = "Strata" + str(index)
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
        self.canvas.create_polygon(corner1[0], corner1[1], corner2[0], corner2[1], corner3[0], corner3[1], corner4[0], corner4[1], fill = self.strataLowlights[index], tags=strataName)

    def InitializeMask(self):
        if(self.mask == []): return
        self.canvas.create_polygon(*self.mask, fill=self.background, tags="Mask")

    def UpdateStrata(self, index):
        strataName = "Strata" + str(index)
        strataValue = index / self.strataCount
        if(strataValue >= (self.value-self.offset)/self.scaleFactor):
            strataColor = self.strataLowlights[index]
        else:
            strataColor = self.strataHighlights[index]
        self.canvas.itemconfigure(strataName, fill=strataColor)

class LabelStat():
    def __init__(self, parent, value=None, highlightPalette = ['#023399'], backgroundPalette = ['#F0F0F0'], paletteDomain=[1], font=("consolas", 10)):
        self.label = Label(parent, font=font)
        self.value             = value
        self.highlightPalette  = highlightPalette
        self.backgroundPalette = backgroundPalette
        self.paletteDomain     = paletteDomain
        self.Set(value)

    def Set(self, value):
        self.value = value
        self.Update()

    def Update(self):
        self.label['text'] = self.GetText()
        self.label['fg'] = self.GetColor(self.highlightPalette,  self.paletteDomain)
        self.label['bg'] = self.GetColor(self.backgroundPalette, self.paletteDomain)
        
    def GetText(self):
        if(self.value == None):
            return "--"
        return str(self.value)

    def GetColor(self, palette, domain):
        if(self.value == None): return palette[0]
        if(len(palette) == 1):  return palette[0]
        for index in range(len(domain)):
            if(self.value < domain[index]):
                return palette[index]
        return palette[len(palette) - 1]

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

class BmsCellStat():
    def __init__(self, parent, width, height, voltageError=['#FFAAAA'], balancePalette=['#F0F0F0'], temperaturePalette=['#FF0000'], voltageDomain=[1], temperatureDomain=[1], fontColor='#000000', font=config.dashFontBareSmall, borderWidth=2):
        self.voltage            = None
        self.balancing          = None
        self.temperature        = None
        self.lowVoltage         = None
        self.viewType           = "Cell"
        self.voltageError       = voltageError
        self.balancePalette     = balancePalette
        self.temperaturePalette = temperaturePalette
        self.voltageDomain      = voltageDomain
        self.temperatureDomain  = temperatureDomain
        self.canvas = Canvas(parent, width=width, height=height, highlightthickness=0)
        self.border     = self.canvas.create_rectangle(0, 0, width, height, width=0, outline="#FFFFFF")
        self.foreground = self.canvas.create_rectangle(borderWidth, borderWidth, width-borderWidth-1, height-borderWidth-1, width=1, outline='#FFFFFF')
        self.text       = self.canvas.create_text(width/2, height/2, fill=fontColor, font=font)
        self.Update()

    def Update(self):
        if(self.viewType == "Cell"):
            self.canvas.itemconfigure(self.border,     fill=self.GetTemperatureColor())
            self.canvas.itemconfigure(self.foreground, fill=self.GetBalanceColor())
            self.canvas.itemconfigure(self.text,       text=self.GetVoltageText())
            self.canvas.itemconfigure(self.foreground, width=1)
        if(self.viewType == "Voltage"):
            self.canvas.itemconfigure(self.border,     fill=self.GetBalanceColor())
            self.canvas.itemconfigure(self.foreground, fill=self.GetBalanceColor())
            self.canvas.itemconfigure(self.text,       text=self.GetVoltageText())
            self.canvas.itemconfigure(self.foreground, width=0)
        if(self.viewType == "Temperature"):
            self.canvas.itemconfigure(self.border,     fill=self.GetTemperatureColor())
            self.canvas.itemconfigure(self.foreground, fill=self.GetTemperatureColor())
            self.canvas.itemconfigure(self.text,       text=self.GetTemperatureText())
            self.canvas.itemconfigure(self.foreground, width=0)
        if(self.viewType == "Delta"):
            self.canvas.itemconfigure(self.border,     fill=self.GetBalanceColor())
            self.canvas.itemconfigure(self.foreground, fill=self.GetBalanceColor())
            self.canvas.itemconfigure(self.text,       text=self.GetDeltaText())
            self.canvas.itemconfigure(self.foreground, width=0)

    def Set(self, voltage, balancing, temperature):
        self.voltage     = voltage
        self.balancing   = balancing
        self.temperature = temperature
        self.Update()

    def SetLowest(self, lowVoltage):
        self.lowVoltage = lowVoltage

    def SetViewType(self, viewType):
        self.viewType = viewType

    def GetVoltageText(self):
        if(self.voltage == None):
            return "--\n--"
        voltage = int(self.voltage*100) / 100
        text = str(voltage)
        while(len(text) < 4):
            text += "0"
        text = text.replace(".", ".\n")
        return text

    def GetDeltaText(self):
        if(self.voltage == None or self.lowVoltage == None):
            return "--"
        delta = self.voltage - self.lowVoltage
        delta = int(delta*100)/100
        text = str(delta)
        while(len(text) < 4):
            text += "0"
        text = text.replace(".", ".\n")
        return text

    def GetTemperatureText(self):
        if(self.temperature == None):
            return "--"
        temperature = int(self.temperature*10)/10
        text = str(temperature)
        return text

    def GetTemperatureColor(self):
        if(self.temperature == None): return self.temperaturePalette[0]
        for index in range(len(self.temperatureDomain)):
            if(self.temperature < self.temperatureDomain[index]):
                if(index <= 0):                           return self.temperaturePalette[0]
                if(index >= len(self.temperatureDomain)): return self.temperaturePalette[index]
                interpolation = InverseLinearInterpolate(self.temperature, self.temperatureDomain[index-1], self.temperatureDomain[index])
                return ColorLinearInterpolate(interpolation, self.temperaturePalette[index-1], self.temperaturePalette[index])
        return self.temperaturePalette[len(self.temperaturePalette)-1]

    def GetBalanceColor(self):
        if(self.balancing == None): return self.balancePalette[0]
        if(self.voltage < self.voltageDomain[0] or self.voltage > self.voltageDomain[1]):
            return self.voltageError
        if(    self.balancing): return self.balancePalette[1]
        if(not self.balancing): return self.balancePalette[2]

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

class CheckStat():
    def __init__(self, parent, value=None, inverted=False, background = '#F0F0F0', foreground='#000000', font=("consolas", 10)):
        self.label = Label(parent, background=background, foreground=foreground, font=font)
        self.value    = value
        self.inverted = inverted

    def Set(self, value):
        self.value = value
        self.Update()

    def Update(self):
        self.label['text'] = self.GetText()
        
    def GetText(self):
        if(self.value == None): return "-"
        if(self.value and not self.inverted): return '\u2713'
        if(not self.value and self.inverted): return '\u2713'
        return 'X'

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

class ButtonBar():
    def __init__(self, parent, width, height, orientation, buttonCommands, buttonLabels=[""], grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", background=config.plainBackground, highlight=config.plainHighlight, fontColor=config.plainFontColor, font=config.plainFontMedium, border=False, borderWidth=config.plainBorderWidth):
        # Root Instantiation
        self.root = Frame(parent, background=background)
        
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
            if(border):
                buttons[index] = Button(self.root, command=buttonCommands[index], text=buttonLabels[index], font=font, foreground=fontColor, background=background, highlightbackground=highlight, highlightthickness=borderWidth)
            if(orientation == "Horizontal"):
                self.root.columnconfigure(index, minsize=buttonWidth)
                buttons[index].grid(column=index, row=0, sticky="NESW")
            if(orientation == "Vertical"):
                self.root.rowconfigure(index, minsize=buttonHeight)
                buttons[index].grid(column=0, row=index, sticky="NESW")

    def Grid(self, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
        self.root.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)

def LinearInterpolate(value, min, max):
    return value * (max - min) + min

def InverseLinearInterpolate(value, min, max):
    return (value - min) / (max - min)

def Clamp(value, min, max):
    if(value > max): return max
    if(value < min): return min
    return value

def ColorLinearInterpolate(value, min, max):
    # Extract Hexadecimal Color Channels to Integer Values
    redMin   = int(min[1:3], 16)
    greenMin = int(min[3:5], 16)
    blueMin  = int(min[5:7], 16)
    redMax   = int(max[1:3], 16)
    greenMax = int(max[3:5], 16)
    blueMax  = int(max[5:7], 16)
    # Interpolate Integer Values and Convert to Hex
    red   = hex(int(Clamp(LinearInterpolate(value, redMin,   redMax),   0, 255)))[2:]
    green = hex(int(Clamp(LinearInterpolate(value, greenMin, greenMax), 0, 255)))[2:]
    blue  = hex(int(Clamp(LinearInterpolate(value, blueMin,  blueMax),  0, 255)))[2:]
    # Insert '0' Padding
    while(len(red)   < 2): red   = '0' + red
    while(len(green) < 2): green = '0' + green
    while(len(blue)  < 2): blue  = '0' + blue
    # Generate Output from Channels
    colorOut = '#' + red + green + blue
    return colorOut