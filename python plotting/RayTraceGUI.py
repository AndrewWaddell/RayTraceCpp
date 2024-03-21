# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:06:37 2024

@author: ihipt
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

class GUI():
    def __init__(self,masterClass=False):
        self.masterClass = masterClass
        self.windowType()
        self.initialiseData()
        self.setTitle()
        self.frames()
        self.buttons()
        self.labels()
        self.entries()
        self.optionMenus()
        self.lamps()
        self.defaults()
        self.initialisePlot()
        self.pack()
        self.mainloop()
    def windowType(self):
        self.window = tk.Tk()
    def setTitle(self):
        self.window.title("New Window")
    def mainloop(self):
        pass
    def initialiseData(self):
        pass
    def frames(self):
        pass
    def buttons(self):
        pass
    def plot(self):
        pass
    def labels(self):
        pass
    def entries(self):
        pass
    def optionMenus(self):
        pass
    def entryVals(self):
        pass
    def lamps(self):
        pass
    def defaults(self):
        pass
    def initialisePlot(self):
        pass
    def pack(self):
        pass
        
        
        

class mainGUI(GUI):
    def mainloop(self):
        self.window.mainloop()
    def setTitle(self):
        self.window.title("Ray Trace")
    def buttons(self):
        self.sourceButton = tk.Button(master=self.window,
                                      text="Create Source",
                                      command=self.createSource)
        self.plotButton = tk.Button(master=self.window,
                                    text="Plot",
                                    command=self.plot)
    def initialiseData(self):
        self.sources = []
    def plot(self):
        print(self.sources)
        y = [i**2 for i in range(int("15"))]
        self.plot1.plot(y)
        self.plotCanvas.draw()
    def initialisePlot(self):
        self.fig = Figure(figsize=(5,5),dpi=100)
        self.plot1 = self.fig.add_subplot(111)
        self.plotCanvas = FigureCanvasTkAgg(self.fig,
                                            master=self.window)
        self.plot()
    def pack(self):
        self.sourceButton.pack()
        self.plotButton.pack()
        self.plotCanvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(self.plotCanvas,self.window)
        toolbar.update()
        self.plotCanvas.get_tk_widget().pack()
    def createSource(self):
        self.sourceWindow = sourceGUI(self)
            

class sourceGUI(GUI):
    def windowType(self):
        self.window = tk.Toplevel()
    def setTitle(self):
        self.window.title("Create Source")
    def buttons(self):
        self.circleButton = tk.Button(master=self.window,
                                      text="Circle",
                                      command=self.makeCircle,
                                      width=12)
        self.rectangleButton = tk.Button(master=self.window,
                                         text="Rectangle",
                                         command=self.makeRectangle,
                                         width=12)
        self.pointButton = tk.Button(master=self.window,
                                     text="Point",
                                     command=self.makePoint,
                                     width=12)
        self.beamButton = tk.Button(master=self.window,
                                    text="Beam",
                                    command=self.makeBeam,
                                    width=12)
        self.createSourceButton = tk.Button(master=self.window,
                                            text="Create Source",
                                            command=self.createSource,
                                            width=12)
    def makeCircle(self):
        self.circleCanvas.itemconfig(self.circleLamp,
                                     state=tk.NORMAL)
        self.rectangleCanvas.itemconfig(self.rectangleLamp,
                                        state=tk.HIDDEN)
    def makeRectangle(self):
        self.circleCanvas.itemconfig(self.circleLamp,
                                     state=tk.HIDDEN)
        self.rectangleCanvas.itemconfig(self.rectangleLamp,
                                        state=tk.NORMAL)
    def makePoint(self):
        self.pointCanvas.itemconfig(self.pointLamp,
                                    state=tk.NORMAL)
        self.beamCanvas.itemconfig(self.beamLamp,
                                   state=tk.HIDDEN)
        self.pointSet = True
    def makeBeam(self):
        self.pointCanvas.itemconfig(self.pointLamp,
                                    state=tk.HIDDEN)
        self.beamCanvas.itemconfig(self.beamLamp,
                                   state=tk.NORMAL)
        self.pointSet = False
    def initialiseData(self):
        self.pointSet = True
    def createSource(self):
        source = {}
        source['density'] = self.densityVal.get()
        source['x'] = self.xVal.get()
        source['y'] = self.yVal.get()
        source['divergence'] = self.divergenceVal.get()
        source['circle'] = True
        source['point'] = self.pointSet
        self.masterClass.sources.append(source)
        self.window.destroy()
    def labels(self):
        self.densityLabel = tk.Label(master=self.window,
                                     text="Density")
        self.xLabel = tk.Label(master=self.window,
                               text="X (diameter)")
        self.yLabel = tk.Label(master=self.window,
                               text="Y")
        self.divergenceLabel = tk.Label(master=self.window,
                                        text="Divergence(deg)")
        self.directionLabel = tk.Label(master=self.window,
                                       text="Direction")
        self.directionXLabel = tk.Label(master=self.xFrame,
                                        text="X")
        self.directionYLabel = tk.Label(master=self.yFrame,
                                        text="Y")
        self.directionZLabel = tk.Label(master=self.zFrame,
                                        text="Z")
    def frames(self):
        self.xFrame = tk.Frame(master=self.window)
        self.yFrame = tk.Frame(master=self.window)
        self.zFrame = tk.Frame(master=self.window)
    def entries(self):
        self.entryVals()
        self.densityEntry = tk.Entry(master=self.window,
                                     textvariable=self.densityVal,
                                     width=5)
        self.xEntry = tk.Entry(master=self.window,
                               textvariable=self.xVal,
                               width=5)
        self.yEntry = tk.Entry(master=self.window,
                               textvariable=self.yVal,
                               width=5)
        self.divergenceEntry = tk.Entry(master=self.window,
                                        width=5)
        self.directionXEntry = tk.Entry(master=self.xFrame,
                                        width=5)
        self.directionYEntry = tk.Entry(master=self.yFrame,
                                        width=5)
        self.directionZEntry = tk.Entry(master=self.zFrame,
                                        width=5)
    def entryVals(self):
        self.densityVal = tk.StringVar()
        self.xVal = tk.StringVar()
        self.yVal = tk.StringVar()
        self.divergenceVal = tk.StringVar()
        self.directionXVal = tk.StringVar()
        self.directionYVal = tk.StringVar()
        self.directionZVal = tk.StringVar()
        self.circleVal = tk.StringVar()
        self.options = ["Circle","Rectangle"]
    def optionMenus(self):
        self.circleOptionMenu = tk.OptionMenu(self.window,
                                              self.circleVal,
                                              *self.options)
    def lamps(self):
        '''Circle lamp'''
        self.circleCanvas = tk.Canvas(self.window,
                                      width=10,
                                      height=10)
        self.circleLamp = self.circleCanvas.create_oval(2,2,10,10)
        self.circleCanvas.itemconfig(self.circleLamp,
                                     fill="red",
                                     outline="black",
                                     state=tk.NORMAL)
        '''Rectangle lamp'''
        self.rectangleCanvas = tk.Canvas(self.window,
                                         width=10,
                                         height=10)
        self.rectangleLamp = self.rectangleCanvas.create_rectangle(2,2,10,10)
        self.rectangleCanvas.itemconfig(self.rectangleLamp,
                                        fill="red",
                                        outline="black",
                                        state=tk.HIDDEN)
        '''Point lamp'''
        self.pointCanvas = tk.Canvas(self.window, width=10, height=10)
        self.pointLamp = self.pointCanvas.create_oval(2,2,10,10)
        self.pointCanvas.itemconfig(self.pointLamp,
                                    fill="red",
                                    outline="black",
                                    state=tk.NORMAL)
        '''Beam lamp'''
        self.beamCanvas = tk.Canvas(self.window,
                                    width=10,
                                    height=10)
        self.beamLamp = self.beamCanvas.create_oval(2,2,10,10)
        self.beamCanvas.itemconfig(self.beamLamp,
                                   fill="red",
                                   outline="black",
                                   state=tk.HIDDEN)
    def defaults(self):
        self.densityEntry.insert(0,"5")
        self.xEntry.insert(0,"15")
        self.yEntry.insert(0,"10")
        self.divergenceEntry.insert(0,"0")
        self.directionXEntry.insert(0,"0")
        self.directionYEntry.insert(0,"0")
        self.directionZEntry.insert(0,"1")
        self.circleVal.set("Circle")
    def pack(self):
        self.densityLabel.grid(row=0,column=0)
        self.densityEntry.grid(row=0,column=1)
        self.circleButton.grid(row=1,column=0)
        self.circleCanvas.grid(row=1,column=1)
        self.rectangleButton.grid(row=2,column=0)
        self.rectangleCanvas.grid(row=2,column=1)
        self.xLabel.grid(row=3,column=0)
        self.xEntry.grid(row=3,column=1)
        self.yLabel.grid(row=4,column=0)
        self.yEntry.grid(row=4,column=1)
        self.pointButton.grid(row=5,column=0)
        self.pointCanvas.grid(row=5,column=1)
        self.beamButton.grid(row=6,column=0)
        self.beamCanvas.grid(row=6,column=1)
        self.divergenceLabel.grid(row=7,column=0)
        self.divergenceEntry.grid(row=7,column=1)
        self.createSourceButton.grid(row=8,column=0)
        self.directionLabel.grid(row=0,column=2)
        self.packXFrame()
        self.packYFrame()
        self.packZFrame()
        self.circleOptionMenu.grid(row=9,column=0)
    def packXFrame(self):
        self.directionXLabel.grid(row=0,column=0)
        self.directionXEntry.grid(row=0,column=1)
        self.xFrame.grid(row=1,column=2)
    def packYFrame(self):
        self.directionYLabel.grid(row=0,column=0)
        self.directionYEntry.grid(row=0,column=1)
        self.yFrame.grid(row=2,column=2)
    def packZFrame(self):
        self.directionZLabel.grid(row=0,column=0)
        self.directionZEntry.grid(row=0,column=1)
        self.zFrame.grid(row=3,column=2)
        
app = mainGUI()