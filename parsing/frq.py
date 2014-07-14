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
        self.detail = self.modify_x()
        
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
    
    def modify_x(self):
        detail = self.x[0]
        for z in range (0, len(self.x)):
            self.x[z] = self.x[z] - detail
        return detail
        
    
#frq('trialdata.frq')