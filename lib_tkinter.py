import tkinter

import json

import enum
from enum import Enum

class Style(dict):
    def __init__(self, filePath=None):
        super().__init__()
        self.__dict__ = self
        self.overrides = dict()
        if(filePath == None):
            self.LoadDefaults()
        else:
            self.LoadJson(filePath)

    def Set(self, key, value):
        self[key] = value

    def LoadDefaults(self):
        # Font
        self.Set("font", ('Consolas', 10))
        # Colors
        self.Set("textColor",  '#000000')   # Black
        self.Set("background", '#F0F0F0')   # Light Grey
        self.Set("highlight",  '#AAAAAA')   # Grey
        self.Set("lowlight",   '#444444')   # Dark Grey
        self.Set("palette",    ['#023399']) # Blue
        # Spacing
        self.Set("padding",     4)
        self.Set("borderWidth", 1)
        # Strata
        self.Set("strataSize",  8)
        self.Set("strataGap",   2)
        self.Set("strataSlope", 0)

    def LoadJson(self, filePath):
        file = open(filePath)
        data = json.load(file)
        for key, item in data.items():
            if(key.__contains__("font")):
                self.Set(key, (item["font"], item["size"]))
            else:
                self.Set(key, item)

    def InsertOverride(self, key1, key2):
        self.overrides[key1] = self[key1]
        self[key1] = self[key2]

    def RemoveOverride(self, key1):
        self[key1] = self.overrides[key1]
        self.overrides.pop(key1)

    def InsertOverrides(self, overrides):
        for key1, key2 in overrides:
            self.InsertOverride(key1, key2)

    def RemoveOverrides(self, overrides):
        for key1, key2 in overrides:
            self.RemoveOverride(key1)

class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL   = 1

# Getters ---------------------------------------------------------------------------------------------------------------------------
def GetFrame(parent, style, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", border=False, styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    frame = tkinter.Frame(parent, background=style['background'])
    padding = 0
    if(border):
        padding = style["padding"]
        frame = tkinter.Frame(parent, background=style["background"], highlightbackground=style["highlight"], padx=padding, pady=padding, highlightthickness=int(style["borderWidth"]))        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky, padx=padding, pady=padding)
    style.RemoveOverrides(styleOverrides)
    return frame

def GetLabelFrame(parent, style, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", label="", border=False, styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    frame = tkinter.LabelFrame(parent, text=label, bg=style["background"], fg=style["textColor"], font=style["font"])
    if(border):
        frame = tkinter.LabelFrame(parent, text=label, bg=style["background"], fg=style["textColor"], font=style["font"], padx=int(style["padding"]), pady=int(style["padding"]), bd=int(style["borderWidth"]))        
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return frame

def GetCanvas(parent, style, width, height, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", border=False, styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    canvas = tkinter.Canvas(parent, width=int(width), height=int(height), background=style["background"], highlightthickness=0)
    if(border):
        canvas = tkinter.Canvas(parent, width=int(width), height=int(height), background=style["background"], highlightbackground=style["highlight"], highlightthickness=int(style["borderWidth"]))
    if(grid):
        canvas.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return canvas

def GetDivider(parent, style, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    frame = tkinter.Frame(parent)
    if(orientation == Orientation.HORIZONTAL):
        divider = tkinter.Canvas(frame, width=2, height=int(style["borderWidth"]), background=style["highlight"], highlightthickness=0)
        divider.pack(fill="both", expand=True)
    if(orientation == Orientation.VERTICAL):
        divider = tkinter.Canvas(parent, width=int(style["borderWidth"]), height=2, background=style["highlight"], highlightthickness=0)
        divider.pack(fill="both", expand=True)
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return frame

def GetLabel(parent, style, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    label = tkinter.Label(parent, font=style["font"], text=text, foreground=style["textColor"], background=style["background"])
    if(grid):
        label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return label

def GetButton(parent, style, command="", text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    button = tkinter.Button(parent, command=command, text=text, font=style["font"], foreground=style["textColor"], background=style["background"])
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return button

def GetImageButton(parent, style, command="", image="", imageSampling=(1,1), grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    
    tkinterImage = tkinter.PhotoImage(file=image)
    if(imageSampling[0] < 1):
        tkinterImage = tkinterImage.subsample(int(1/imageSampling[0]), 1)
    else:
        tkinterImage = tkinterImage.zoom(int(imageSampling[0]), 1)
    if(imageSampling[1] < 1):
        tkinterImage = tkinterImage.subsample(1, int(1/imageSampling[1]))
    else:
        tkinterImage = tkinterImage.zoom(1, int(imageSampling[1]))

    button = tkinter.Button(parent, command=command, image=tkinterImage, foreground=style["textColor"], background=style["background"])
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return (button, tkinterImage)

def GetRadiobutton(parent, style, value="", variable="", text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    button = tkinter.Radiobutton(parent, variable=variable, value=value, text=text, font=style["font"], foreground=style["textColor"], background=style["background"])
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def GetEntry(parent, style, minWidth, value="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    entry = tkinter.Entry(parent, width=minWidth, font=style["font"], foreground=style["textColor"], bg=style["background"])
    entry.insert(0,str(value))
    if(grid): entry.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return entry

def GetCheckbutton(parent, style, variable, text="", grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky=""):
    button = tkinter.Checkbutton(parent, variable=variable, text=text, font=style["font"], foreground=style["textColor"], background=style["background"])
    if(grid): button.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return button

def GetProgressBar(parent, style, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", minWidth=20, minHeight=20, gridPadding=0, scaleFactor=1, offset=0, label="", border=False, styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    bar = ProgressBar(parent, orientation, minWidth=minWidth, minHeight=minHeight, scaleFactor=scaleFactor, offset=offset, label=label, background=style["background"], outline='#000000', foreground=style["lowlight"], font=style["font"], textColor=style["textColor"], borderWidth=0)
    if(border):
        bar = ProgressBar(parent, orientation, minWidth=minWidth, minHeight=minHeight, scaleFactor=scaleFactor, offset=offset, label=label, background=style["background"], outline=style["highlight"], foreground=style["lowlight"], font=style["font"], textColor=style["textColor"], borderWidth=style["borderWidth"])
    if(grid):
        bar.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky, padx=gridPadding, pady=gridPadding)
    style.RemoveOverrides(styleOverrides)
    return bar

def GetStrataBar(parent, style, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", minWidth=20, minHeight=20, scaleFactor=1, offset=0, border=False, highlights=["#023399"], lowlights=["#F0F0F0"], domain=[1], mask=[], styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    bar = StratifiedBar(parent, orientation, minWidth=minWidth, minHeight=minHeight, scaleFactor=scaleFactor, offset=offset, background=style["background"], highlights=highlights, lowlights=lowlights, domain=domain, strataSize=style["strataSize"], strataGap=style["strataGap"], borderWidth=0)
    if(border):
        bar = StratifiedBar(parent, orientation, minWidth=minWidth, minHeight=minHeight, scaleFactor=scaleFactor, offset=offset, background=style["background"], highlights=highlights, lowlights=lowlights, domain=domain, strataSize=style["strataSize"], borderWidth=style["borderWidth"], borderColor=style["highlight"])
    
    bar.ShearStrata(style["strataSlope"])
    if(len(mask) >= 2):
        bar.MaskStrata(mask[0], mask[1], *mask[2:])
    
    if(grid):
        bar.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return bar

def GetButtonBar(parent, style, orientation, commands, labels=[], grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", minWidth=20, minHeight=20, border=False, styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    bar = ButtonBar(parent, orientation, commands, minWidth=minWidth, minHeight=minHeight, labels=labels, background=style["background"], borderColor='#000000', font=style["font"], fontColor=style["textColor"], borderWidth=0)
    if(border):
        bar = ButtonBar(parent, orientation, commands, minWidth=minWidth, minHeight=minHeight, labels=labels, background=style["background"], borderColor=style["highlight"], font=style["font"], fontColor=style["textColor"], borderWidth=style["borderWidth"])
    if(grid):
        bar.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return bar

def GetLabelStat(parent, style, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", precision=0, fontColors=None, domain=[1], styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    if(fontColors == None):
        fontColors = [style["textColor"]]
    label = LabelStat(parent, precision=precision, fontColors=fontColors, background=style["background"], domain=domain, font=style["font"])
    if(grid):
        label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return label

def GetCheckStat(parent, style, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", inverted=False, styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    stat = CheckStat(parent, inverted=inverted, foreground=style["textColor"], background=style["background"], font=style["font"])
    if(grid):
        stat.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return stat

def GetScrollFrame(parent, style, orientation, grid=True, column=0, row=0, columnspan=1, rowspan=1, sticky="", styleOverrides=[]):
    style.InsertOverrides(styleOverrides)
    frame = ScrollFrame(parent, orientation=orientation, background=style["background"], highlight=style["highlight"])
    if(grid):
        frame.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    style.RemoveOverrides(styleOverrides)
    return frame

# Widgets ---------------------------------------------------------------------------------------------------------------------------
class ProgressBar(tkinter.Canvas):
    def __init__(self, parent, orientation, minWidth=20, minHeight=20, scaleFactor=1, offset=0, label="", background='#F0F0F0', outline='#AAAAAA', foreground='#444444', font=("consolas", 10), textColor="#000000", borderWidth=1):
        # Initialize Variables
        self.width       = minWidth
        self.height      = minHeight
        self.scaleFactor = scaleFactor
        self.offset      = offset
        self.orientation = orientation
        self.value       = None
        
        # Root
        super().__init__(parent, width=self.width, height=self.height, background=background, highlightthickness=borderWidth, highlightbackground=outline)
        self.bar   = self.create_rectangle(0, 0, self.width, self.height, fill=foreground, width=0)
        self.label = self.create_text(0, 0, fill=textColor, font=font, text=self.FormatText(label))

        # Interrupts
        self.bind("<Configure>", self.Redraw)

    def Redraw(self, event):
        self.width  = event.width
        self.height = event.height
        self.RedrawBar()
        self.RedrawLabel()

    def RedrawBar(self):
        if(self.orientation == Orientation.VERTICAL):
            self.coords(self.bar, 0, self.height, self.width, self.height * (1-self.GetPercent()))
        if(self.orientation == Orientation.HORIZONTAL):
            self.coords(self.bar, 0, 0, self.width * self.GetPercent(), self.height)

    def RedrawLabel(self):
        self.coords(self.label, self.width / 2, self.height / 2)

    def FormatText(self, text):
        if(len(text) <= 1): return text
        if(self.orientation == Orientation.HORIZONTAL): return text
        if(self.orientation == Orientation.VERTICAL):
            output = ""
            for index in range(len(text) - 1):
                output += text[index] + '\n'
            output += text[len(text) - 1]
            return output
        return ""

    def GetPercent(self):
        if(self.value == None): return 0
        return (self.value - self.offset) / self.scaleFactor

    def Set(self, value):
        if(value == None): return
        self.value = value
        self.RedrawBar()

    def Get(self):
        return self.value

class StratifiedBar(tkinter.Canvas):
    def __init__(self, parent, orientation, minWidth=20, minHeight=20, scaleFactor=1, offset=0, background='#F0F0F0', highlights = ['#023399'], lowlights = ['#F0F0F0'], domain = [1], strataSize = 8, strataGap = 2, borderWidth = 1, borderColor='#AAAAAA'):
        # Initialize Variables
        self.width            = minWidth
        self.height           = minHeight
        self.scaleFactor      = scaleFactor
        self.offset           = offset
        self.orientation      = orientation
        self.strataSize       = strataSize
        self.strataGap        = strataGap
        self.strata           = []
        self.mask             = None
        self.maskX0           = None
        self.maskY0           = None
        self.maskCoords       = None
        self.strataSlope      = 0
        self.strataCount      = 0
        self.background       = background
        self.domain           = domain
        self.highlights       = highlights
        self.lowlights        = lowlights
        self.value            = None

        # Root
        super().__init__(parent, width=self.width, height=self.height, bg=background, highlightthickness=borderWidth, highlightbackground=borderColor)

        # Interrupts
        self.bind("<Configure>", self.Redraw)

    def Redraw(self, event):
        self.width  = event.width
        self.height = event.height
        self.RedrawStrata()
        self.RedrawMask()

    def RedrawStrata(self):
        if(self.orientation == Orientation.VERTICAL):
            return
        if(self.orientation == Orientation.HORIZONTAL):
            self.strataCount = 0
            cumulativeWidth = 0
            
            while(True):
                if(self.strataCount != 0):
                    cumulativeWidth += self.strataGap
                cumulativeWidth += self.strataSize 
                if(cumulativeWidth < self.width):
                    self.strataCount += 1
                else:
                    cumulativeWidth -= self.strataGap
                    cumulativeWidth -= self.strataSize
                    break
            
            self.strataOffset = int((self.width - cumulativeWidth) / 2)

        for stratum in self.strata:
            self.delete(stratum)
        self.strata = []

        self.ShearStrata(self.strataSlope)
        self.GenerateStrataPalette()
        
        for stratumIndex in range(self.strataCount):
            self.RedrawStratum(stratumIndex)

    def RedrawStratum(self, index):
        if(self.orientation == Orientation.VERTICAL):
            return
        if(self.orientation == Orientation.HORIZONTAL):
            x0 = index * (self.strataSize + self.strataGap) + self.strataOffset + self.strataSlope * self.height
            y0 = 0
            x1 = x0 + self.strataSize
            y1 = y0
            x2 = x1 - self.strataSlope * self.height
            y2 = self.height
            x3 = x0 - self.strataSlope * self.height
            y3 = y2
            stratum = self.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3)
            self.strata.append(stratum)
        self.ColorStratum(index)

    def ColorStratum(self, index):
        stratumPercent = index / self.strataCount
        if(stratumPercent < self.GetPercent()):
            self.itemconfigure(self.strata[index], fill=self.strataHighlights[index])
        else:
            self.itemconfigure(self.strata[index], fill=self.strataLowlights[index])

    def GenerateStrataPalette(self):
        self.strataHighlights = []
        self.strataLowlights  = []
        for strataIndex in range(self.strataCount):
            for domainIndex in range(len(self.domain)):
                normalizedDomain = (self.domain[domainIndex] - self.offset) / self.scaleFactor
                if(strataIndex / self.strataCount < normalizedDomain):
                    self.strataHighlights.append(self.highlights[domainIndex])
                    self.strataLowlights.append(self.lowlights[domainIndex])
                    break

    def Set(self, value):
        if(value == None): return
        self.value = value

    def GetPercent(self):
        if(self.value == None): return 0
        return (self.value - self.offset) / self.scaleFactor

    def Get(self):
        return self.value

    def ShearStrata(self, slope):
        if(slope == 0): return
        self.strataSlope = slope
        if(self.orientation == Orientation.HORIZONTAL):
            strataLossCount = int(slope * self.height / (self.strataSize + self.strataGap)) + 1
            if(strataLossCount >= self.strataCount):
                self.strataCount = 0
            else:
                self.strataCount -= strataLossCount

    def MaskStrata(self, x0, y0, *xyCoords):
        self.maskX0 = x0
        self.maskY0 = y0
        self.maskCoords = xyCoords
        self.mask = self.create_polygon(0, 0)
        self.RedrawMask()

    def RedrawMask(self):
        if(self.maskX0 == None or self.maskY0 == None): return

        x0 = self.maskX0 * self.width
        y0 = self.maskY0 * self.height

        xyCoords = []
        for index in range(len(self.maskCoords)):
            if(index & 2 == 0): # X
                xyCoords.append(self.maskCoords[index] * self.width)
            else: # Y
                xyCoords.append(self.maskCoords[index] * self.height)

        self.delete(self.mask)
        self.mask = self.create_polygon(x0, y0, xyCoords, fill=self.background)

class ButtonBar(tkinter.Frame):
    def __init__(self, parent, orientation, commands, minWidth=20, minHeight=20, labels=[], background="#F0F0F0", fontColor="#000000", font=("consolas", 10), borderColor="#444444", borderWidth=1):
        # Root Instantiation
        super().__init__(parent, background=background, width=minWidth, height=minHeight, highlightthickness=borderWidth, highlightcolor=borderColor)
        
        # Root Partitioning
        buttonCount = len(commands)
            
        # Button Data
        buttons = [None] * buttonCount
        if(labels == []):
            labels = [""] * buttonCount
            
        # Root Widgets
        for index in range(buttonCount):
            if(orientation == Orientation.HORIZONTAL):
                self.columnconfigure(index, weight=1)
                container = tkinter.Frame(self, height=minHeight, background=background, highlightbackground=borderColor, highlightthickness=borderWidth)
                container.pack_propagate(0)
                container.grid(column=index, row=0, sticky="NESW")
                buttons[index] = tkinter.Button(container, command=commands[index], text=labels[index], font=font, foreground=fontColor, background=background, highlightbackground=borderColor, highlightthickness=borderWidth)
                buttons[index].pack(expand=True, fill="both")
            if(orientation == Orientation.VERTICAL):
                self.rowconfigure(index, weight=1)
                container = tkinter.Frame(self, width=minWidth, background=background, highlightbackground=borderColor, highlightthickness=borderWidth)
                container.pack_propagate(0)
                container.grid(column=0, row=index, sticky="NESW")
                buttons[index] = tkinter.Button(container, command=commands[index], text=labels[index], font=font, foreground=fontColor, background=background, highlightbackground=borderColor, highlightthickness=borderWidth)
                buttons[index].pack(expand=True, fill="both")

class LabelStat(tkinter.Label):
    def __init__(self, parent, precision=0, fontColors=['#023399'], background='#F0F0F0', domain=[1], font=("consolas", 10)):
        super().__init__(parent, font=font, foreground=fontColors[0], background=background,  text="--")
        self.precision   = precision
        self.fontColors  = fontColors
        self.domain      = domain
        self.value       = None

    def Set(self, value):
        self.value = value
        self.Update()

    def Update(self):
        self['text'] = self.GetText()
        self['fg']   = self.GetColor(self.fontColors, self.domain)
        
    def GetText(self):
        if(self.value == None): return "--"
        if(self.precision == 0): return str(int(self.value))
        return str(int(self.value * 10 ** self.precision) / 10 ** self.precision)

    def GetColor(self, palette, domain):
        if(self.value == None): return palette[0]
        if(len(palette) == 1):  return palette[0]
        for index in range(len(domain)):
            if(self.value < domain[index]):
                return palette[index]
        return palette[len(palette) - 1]

class CheckStat(tkinter.Label):
    def __init__(self, parent, inverted=False, background = '#F0F0F0', foreground='#000000', font=("consolas", 10)):
        super().__init__(parent, background=background, foreground=foreground, font=font, text="-")
        self.value    = None
        self.inverted = inverted

    def Set(self, value):
        self.value = value
        self.Update()

    def Update(self):
        self['text'] = self.GetText()
        
    def GetText(self):
        if(self.value == None): return "-"
        if(self.value and not self.inverted): return '\u2713'
        if(not self.value and self.inverted): return '\u2713'
        return 'X'

class ScrollFrame(tkinter.Frame):
    def __init__(self, parent, orientation, background="#F0F0F0", highlight="#AAAAAA"):
        super().__init__(parent, background=background, highlightthickness=0)

        self.orientation = orientation

        if(orientation == Orientation.VERTICAL):
            self.scrollbar = tkinter.Scrollbar(self, orient="vertical", background=background, highlightcolor=highlight)
            self.scrollbar.pack(fill="y", side="right", expand=False)
        
            self.canvas = tkinter.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=self.scrollbar.set, background=background, highlightcolor=highlight)
            self.canvas.pack(side="left", fill="both", expand=True)
        
            self.scrollbar.config(command=self.canvas.yview)
        if(orientation == Orientation.HORIZONTAL):
            self.scrollbar = tkinter.Scrollbar(self, orient="horizontal", background=background, highlightcolor=highlight)
            self.scrollbar.pack(fill="x", side="bottom", expand=False)
        
            self.canvas = tkinter.Canvas(self, bd=0, highlightthickness=0, xscrollcommand=self.scrollbar.set, background=background, highlightcolor=highlight)
            self.canvas.pack(side="top", fill="both", expand=True)
        
            self.scrollbar.config(command=self.canvas.xview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.frame  = tkinter.Frame(self.canvas, background=background, highlightcolor=highlight)
        self.frameWindow = self.canvas.create_window(0, 0, window=self.frame, anchor="nw")

        self.frame.bind('<Configure>', self.RedrawFrame)

        self.canvas.bind('<Configure>', self.RedrawCanvas)

    def RedrawFrame(self, event):
        width  = self.frame.winfo_reqwidth()
        height = self.frame.winfo_reqheight()
        self.canvas.config(scrollregion=(0, 0, width, height))
        if(self.orientation == Orientation.VERTICAL and width != self.canvas.winfo_width()):
            self.canvas.config(width=width)
        if(self.orientation == Orientation.HORIZONTAL and height != self.canvas.winfo_height()):
            self.canvas.config(height=height)

    def RedrawCanvas(self, event):
        if(self.orientation == Orientation.VERTICAL and self.frame.winfo_reqwidth() != self.canvas.winfo_width()):
            self.canvas.itemconfigure(self.frameWindow, width=self.canvas.winfo_width())
        if(self.orientation == Orientation.HORIZONTAL and self.frame.winfo_reqheight() != self.canvas.winfo_height()):
            self.canvas.itemconfigure(self.frameWindow, height=self.canvas.winfo_height())

    def Get(self):
        return self.frame
