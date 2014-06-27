'''
Created on Jun 27, 2014

@author: Ian
'''
import wx
import menuActions
import mainGraphic

class primaryFrame(wx.Frame):
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (650, 500))
        self.initComponents()
        
        self.Show(True)
        
    def initComponents(self):
        self.initGraphic()
        self.initPanels()
        self.initMenu()
        
    def initGraphic(self):
        self.image = mainGraphic.mainGraphic(self)
        self.control = self.image
        
    def initPanels(self):
        print 'implement initPanels'
        
    def initMenu(self):
        self.filemenu = wx.Menu()
        self.filemenu.AppendSeparator()
        self.menuExit = self.filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the Program")
        
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.filemenu, "&File")
        self.SetMenuBar(self.menuBar)
        
        self.bindActions()
    
    def bindActions(self):
        self.Bind(wx.EVT_MENU, menuActions.onExit(self), self.menuExit)
        
app = wx.App(False)
frame = primaryFrame(None, 'Earth Wind and Fire')
app.MainLoop()