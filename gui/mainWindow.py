'''
Created on Jun 27, 2014

@author: Ian
'''

import wx
import menuActions
import mainGraphic
import matplotlib.pyplot as plt

class primaryFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (650, 500))
        self.initComponents()
        
        self.Show(True)
        
    def initComponents(self):
        self.initGraphic()
        self.initPanels()
        self.initMenus()
        
    def initGraphic(self):
        self.panel = mainGraphic.mainGraphic(self)
        
    def initPanels(self):
        print 'implement initPanels'
        
    def initMenus(self):
        self.initFileMenu()
        self.initParseMenu()
        self.initDataMenu()
        self.initAnalysisMenu()
        self.initMenuBar()
        self.bindActions()
        
    def initFileMenu(self):
        self.fileMenu = wx.Menu()
        self.menuOpen = self.fileMenu.Append(wx.ID_OPEN, "&Open", " Open an already parsed Data File")
        self.menuSave = self.fileMenu.Append(wx.ID_SAVE, "&Save", " Save a Data File")
        self.fileMenu.AppendSeparator()
        self.menuExit = self.fileMenu.Append(wx.ID_EXIT, "&Exit", " Terminate the Program")
        self.menuAbout = self.fileMenu.Append(wx.ID_ABOUT, "&About", " Information about the Program")
        
    def initParseMenu(self):
        self.parseMenu = wx.Menu()
        self.menuFromLV = self.parseMenu.Append(wx.ID_ANY, "&From LabView", " Parse in a LabView Data Set (input: two arrays of double)")
        self.menuFromSAC = self.parseMenu.Append(wx.ID_ANY, "From SAC", " Parse in a SAC Data Set (input: )")
        
    def initDataMenu(self):
        self.dataMenu = wx.Menu()
        self.initInterMenu()
#         self.initAnalysisMenu()
#         self.init
        self.dataMenu.AppendSubMenu(self.interMenu, "&Interpolate", " 'Fill in the gaps' of a data file")
        self.plotMenu = self.dataMenu.Append(wx.ID_ANY, "&Plot", " Plot Current Data Set")
        
    def initInterMenu(self):
        self.interMenu = wx.Menu()
        self.menuConstant = self.interMenu.Append(wx.ID_ANY, "&Constant Value", "Interpolate")
    
    def initAnalysisMenu(self):
        self.analysisMenu = wx.Menu()
        self.menuSimple = self.analysisMenu.Append(wx.ID_ANY, "&Simple Analysis", "find Mean Median and Mode of current data set")
        
    def initMenuBar(self):
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, "&File")
        self.menuBar.Append(self.parseMenu, "&Parse")
        self.menuBar.Append(self.dataMenu, "&Data")
        self.menuBar.Append(self.analysisMenu, "&Analysis")
        self.SetMenuBar(self.menuBar)
        
    def bindActions(self):
        self.Bind(wx.EVT_MENU, self.onExit, self.menuExit)
        self.Bind(wx.EVT_MENU, self.openFRQ, self.menuFromLV)
        self.Bind(wx.EVT_MENU, self.sAnal, self.menuSimple)
        self.Bind(wx.EVT_MENU, self.plot, self.menuPlot)
        
    def onExit(self, e):
        self.Close()
        
    def openFRQ(self, e):
        self.original_data = menuActions.openLV(self)
        self.current_data = self.original_data
        self.plot(self.original_data)
        
    def sAnal(self, e):
        menuActions.simpleAnalysis(self.current_data)
        
    def plot(self, e):
        menuActions.plot(self.current_data)
        
app = wx.App(False)
frame = primaryFrame(None, 'Earth Wind and Fire')
panel = mainGraphic.mainGraphic(frame)
frame.Show()
app.MainLoop()