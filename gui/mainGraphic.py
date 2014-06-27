'''
Created on Jun 27, 2014

@author: Ian
'''
import wx

class mainGraphic(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent
        
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
    
    def OnEraseBackground(self, e):
        dc = e.GetDC()
        
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect()
        dc.Clear()
        bmp = wx.Bitmap("main.jpg")
        dc.DrawBitmap(bmp, 0, 0)