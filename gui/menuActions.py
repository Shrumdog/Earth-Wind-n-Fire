'''
Created on Jun 30, 2014

@author: Ian
'''
import wx
import os
import parsing.fromLabView as parseLV
    
def openLV(frame):
    dirname=''
    dlg = wx.FileDialog(frame, "Select data to parse in", dirname, "", "*.frq", wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        filename = dlg.GetFilename()
        dirname = dlg.GetDirectory()
        f = os.path.join(dirname, filename)
        print dirname
        print filename
    dlg.Destroy()
    parseLV.LV(f)