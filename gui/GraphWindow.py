'''
Created on Jul 8, 2014

@author: Ian
'''
import wx
import matplotlib as mpl
import matplotlib.backends as backends
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class window(wx.Frame):
    def __init__(self, parent, data):
        wx.Frame.__init__(self, parent, title="Working Title", size=(1000,600))
        self.data = data
        self.init_panel()
        self.init_menus()
        self.Show()
    
    def init_panel(self):
        self.panel = wx.Panel(self)
        self.refresh = wx.Button(self.panel, label="Update")
        
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.refresh)
        
        self.graph = panel(self, position=(20, 50))
        self.graph.update(self.data)
        self.panel.SetSizerAndFit(self.sizer)
    
    def init_menus(self):
        print 'write init_menus'
        
    def GetData(self):
        return self.data

class panel(wx.Panel):
    def __init__(self, parent, position):
        wx.Panel.__init__(self, parent,pos=position, size=(800, 320))
        self.data=parent.GetData()
        self.init_mpl()
        
    def init_mpl(self):
        self.figure = mpl.figure.Figure(None, facecolor='white')
        self.canvas = backends.backend_wxagg.FigureCanvasWxAgg(self, -1, self.figure)
        self.axes = self.figure.add_subplot(111)
        self.axes.grid(True, color='gray')
        self.axes.set_xbound( (0, len(self.data[0])) )
        self.axes.set_ybound( (0, 500) )
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Hz')
        self.axes = self.figure.add_subplot(111)
        self.axes.grid(True, color='gray')
        self._SetSize()
        self.Bind(wx.EVT_SIZE, self._SetSize)
        
    def update(self, data):
        x = data[0]
        y = data[1]
        
        yMin = round(min(y)) - 5
        yMax = round(max(y)) + 5
        self.axes.plot(x,y,"-k")
        self.axes.set_ybound( (yMin,yMax) )
        self.canvas = FigureCanvas(self, -1, self.figure)
        
    def _SetSize(self, event=None):
        pixels = self.GetSize()
        self.SetSize(pixels)
        self.canvas.SetSize(pixels)
        
        dpi = self.figure.get_dpi()
        self.figure.set_size_inches(float(pixels[0]) / dpi, float(pixels[1]))