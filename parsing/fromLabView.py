'''
Created on Jun 30, 2014

@author: Ian
'''
import numpy as np

class LV():
    
    def __init__(self, f):
        file = open(f, 'r+')
        contents = file.read()
        file.close()
        
        print len(contents)
        print contents[0]
        
        blah = np.fromfile(f, float, -1, "")
        print len(blah)
        print blah[0]
        print blah[36000]
        x, y = self.split_data(blah)
        print x[0]
        print y[0]
        print y[1]
        print y[2]
        
    def split_data(self, arr):
        x = []
        y = []
        for z in range(0, len(arr)):
            if (z < len(arr)/2):
                x.append(arr[z])
            else:
                y.append(arr[z])
        return (x, y)
    
LV('trialdata.frq')