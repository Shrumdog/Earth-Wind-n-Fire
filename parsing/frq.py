'''
Created on Jun 30, 2014

@author: Ian
'''
import numpy as np

class frq():
    
    def __init__(self, f):        
        blah = np.fromfile(f, float, -1, "")
        blah = blah.byteswap()
        self.x, self.y = self.split_data(blah)
        
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
    
#frq('trialdata.frq')