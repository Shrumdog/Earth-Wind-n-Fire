'''
Created on Jun 30, 2014

@author: Ian
'''
import wx
import os
import parsing.frq as parseFRQ
import numpy as np
import matplotlib.pyplot as plt
import decimal
import parsing
    
def openLV():
    app = wx.App(False)
    dirname=''
    dlg = wx.FileDialog(None, "Select data to parse in", dirname, "", "*.frq", wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
        filename = dlg.GetFilename()
        print filename
        dirname = dlg.GetDirectory()
        print dirname
        f = os.path.join(dirname, filename)
    dlg.Destroy()
    data = parseFRQ.frq(f).GetData()
    xdata = bucket(data[1])
    return data[0], xdata

def simpleAnalysis(data):
#     data = data[1]
#     for b in range (0, 20):
#     print "Bucket Size: " + str(b)
    op_data = bucket(data) 
    
    mean = np.mean(op_data)
    median = np.median(op_data)
    modes = dict()
    for x in range(0, len(op_data)):
        if(modes.has_key(op_data[x])):
            this = modes.pop(op_data[x])
            this += 1
            modes.update({op_data[x]:this})
        else:
            modes.update({op_data[x]:1})
        iter = modes.iteritems()
        op = iter.next()
        curmax = 0
        mode = 0
        hits = 0
        while(True):
            hits += op[1]
            if(op[1] > curmax):
                curmax = op[1]
                mode = op[0]
            try:
                op = iter.next()
            except StopIteration:
                break
    print "total hits: " + str(hits)
    print "length of set: " + str(len(modes))
    average_hits = float(hits)/len(modes)
    print "mean: " + str(mean)
    print "median: " + str(median)
    print "mode: " + str(mode)
    print "max hits: " + str(curmax)
    print "average hits: " + str(average_hits)
    
def bucket(data):
    new = []
    for x in data:
        new.append(float("%.5f" % x))
    return new
    
def plot(data):
    plt.plot(data[0], data[1])
    yMin = round(min(data[1])) - 5
    yMax = round(max(data[1])) + 5
    xMax = data[0][len(data[0]) - 1] + 5
    plt.axis([0, xMax, yMin, yMax])
    plt.show()
    
# name = os.path.join("C:\Users\Ian\Desktop\Folder Folder\EWF\DataSets", "2014-06-24-20-59-46.frq")
# f = parsing.frq.frq(name)
# data = f.GetData()
# simpleAnalysis(data)