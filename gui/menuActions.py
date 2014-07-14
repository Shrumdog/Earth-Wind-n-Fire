'''
Created on Jun 30, 2014

@author: Ian
'''
import wx
import os
import parsing.frq as parseFRQ
import numpy as np
import matplotlib.pyplot as plt
    
def openLV(frame):
    dirname=''
    dlg = wx.FileDialog(frame, "Select data to parse in", dirname, "", "*.frq", wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        filename = dlg.GetFilename()
        dirname = dlg.GetDirectory()
        f = os.path.join(dirname, filename)
    dlg.Destroy()
    return parseFRQ.frq(f).GetData()

def simpleAnalysis(data):
    data = data[1]
    mean = np.mean(data)
    median = np.median(data)
    modes = dict()
    for x in range(0, len(data)):
        if(modes.has_key(data[x])):
            print "Has key " + data[x]
            this = modes.get(data[x])
            print "Old value: " + this
            this += 1
            print "Updating to " + this
            print "New value: " + modes.get(data[x])
        else:
            modes.update({data[x]:1})
    iter = modes.iteritems()
    op = iter.next()
    curmax = 0
    mode = 0
    while(op != None):
        if(op[1] > curmax):
            curmax = op[1]
            mode = op[0]
        try:
            op = iter.next()
        except StopIteration:
            break
    print "mean: " + str(mean)
    print "median: " + str(median)
    print "mode: " + str(mode)
    
def plot(data):
    plt.plot(data[0], data[1])
    yMin = round(min(data[1])) - 5
    yMax = round(max(data[1])) + 5
    xMax = data[0][len(data[0]) - 1] + 5
    plt.axis([0, xMax, yMin, yMax])
    plt.show()