'''
Created on Jun 27, 2014

@author: Ian
'''

import wx
import menuActions
import mainGraphic
import GraphWindow

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
    
    def initInterMenu(self):
        self.interMenu = wx.Menu()
        self.menuConstant = self.interMenu.Append(wx.ID_ANY, "&Constant Value", "Interpolate")
        
    def initMenuBar(self):
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.fileMenu, "&File")
        self.menuBar.Append(self.parseMenu, "&Parse")
        self.menuBar.Append(self.dataMenu, "&Data")
        self.SetMenuBar(self.menuBar)
        
    def bindActions(self):
        self.Bind(wx.EVT_MENU, self.onExit, self.menuExit)
        self.Bind(wx.EVT_MENU, self.openFRQ, self.menuFromLV)
        
    def onExit(self, e):
        self.Close()
        
    def openFRQ(self, e):
        self.xdata, self.ydata = menuActions.openLV(self)
        GraphWindow.window(self,(self.xdata,self.ydata))
        
app = wx.App(False)
frame = primaryFrame(None, 'Earth Wind and Fire')
panel = mainGraphic.mainGraphic(frame)
frame.Show()
app.MainLoop()