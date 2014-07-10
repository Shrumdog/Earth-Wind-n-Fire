'''
Created on Jun 30, 2014

@author: Ian
'''
import numpy as np

class frq():
    
    def __init__(self, f):        
        blah = np.fromfile(f, float, -1, "")
        blah = blah.byteswap()
        self.y, self.x = self.split_data(blah)
        self.x, self.detail = self.modify(self.x)
        
    def split_data(self, arr):
        x = []
        y = []
        for z in range(0, len(arr)):
            if (z < len(arr)/2):
                x.append(arr[z])
            else:
                y.append(arr[z])
        return (x, y)
    
    def GetData(self):
        return self.x, self.y
    
    def GetDetail(self):
        return self.detail
    
    def modify(self, arr):
        modifier = arr[0]
        for x in range(0, len(arr)):
            arr[x] = arr[x] - modifier
        return (arr, modifier)
    
#frq('trialdata.frq')