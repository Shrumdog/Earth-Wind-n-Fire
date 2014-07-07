'''
Created on Jun 27, 2014

@author: Ian
'''
import wx

class mainGraphic(wx.Panel):
    
    def __init__(self, parent, bg_img = 'main.jpg'):
        wx.Panel.__init__(self, parent=parent)
        bmp1 = wx.Image(bg_img, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
