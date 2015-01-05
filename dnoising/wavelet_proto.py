'''
Created on Jul 14, 2014

@author: Ian
'''
import math
import gui.menuActions as ma

class wave(object):
    
    def __init__(self, arr, pow):
        self.original = arr
        self.cur_pow = 1
        self.arr = []
        
        for x in range (0, len(arr)/2):
            dif = diff(arr[2 * x], arr[2 * x + 1])
            self.arr.append([dif[0], dif[1]])
            
        while(self.cur_pow < pow):
            self.nxt_pow()
        
    def inc_pow(self):
        self.cur_pow += 1
        
    def nxt_pow(self):
        cur_pow = self.cur_pow
        arr = self.arr
        new = [[0 for x in xrange(int(math.pow(2, cur_pow + 1)))] for x in xrange(len(arr)/2)]
        for x in range(0, len(arr)/2):
            index = 2 * x
            left = arr[index]
            right = arr[index + 1]
            new[x] = merge_wave(left, right)
        
        self.inc_pow()
        self.arr = new
        
    def get_diffs(self, pow): #here the power is the power of the set of differences to retrieve
        if pow > self.cur_pow:
            return None
        num = int(len(self.arr[0]) / math.pow(2, pow))
        start = int(math.pow(2, self.cur_pow - pow))
        
        new = []
        for a in self.arr:
            for x in range(start, start + num):
                new.append(a[x])
                
        return new
    
    def set_diffs(self, arr):
        pow = (len(self.arr[0]) * len(self.arr)) / len(arr) - 1
        size = int(math.pow(2, self.cur_pow) / (pow + 1))
        start = int(math.pow(2, self.cur_pow - pow))
        
        op = []
        for a in range (0, size):
            op.append(arr[a])
            if (len(op) % size == 0):
                for x in range (start, start + size):
                    self.arr[a/size][x] = op[x - start]
                op = []
        
        
    def thresh(self, pow, hi = 50, lo = 0.01):
        arr = self.get_diffs(pow)
        for a in arr:
            if (a > hi or a < lo):
                a = 0.0
        self.set_diffs(arr)
                
        
    def reconstruct(self):
        pow = int(math.log(len(self.arr[0]), 2))
        final = []
        
        for z in range(0, len(self.arr)):
            new = []
            for x in self.arr[z]:
                new.append(x)
            
            for x in range (0, pow):
                ups = []
                for y in range (0, int(math.pow(2, x))):
                    detail = int(y + math.pow(2, x))
                    
                    ups.append(new[y] + (new[detail] / 2))
                    ups.append(new[y] - (new[detail] / 2))
                for h in range(0, len(ups)):
                    new[h] = ups[h]
                    
            for x in new:
                final.append(x)
        
        self.arr = final
        
def diff(x, y):
    return ((x+y)/2), (x-y)
        
def merge_wave(left, right):
    new = []
    dif = diff(left[0], right[0])
    new.append(dif[0])  #grab the averages
    new.append(dif[1])
    for x in range (0, int(math.log(len(left), 2))):
        for y in range(0, int(math.pow(2, x))):
            new.append(left[int(math.pow(2, x) + y)])
        for y in range(0, int(math.pow(2, x))):
            new.append(right[int(math.pow(2, x) + y)])
    return new
            
def merge_sets(left, right):
    new = []
    for x in range (0, int(math.log(len(left), 2))):
        for y in range(0, int(math.pow(2, x))):
            new.append(left[math.pow(2, x) + y])
        for y in range(0, int(math.pow(2, x))):
            new.append(right[math.pow(2, x) + y])
    return new

def plot(data):
    xdata = data[1]
    ydata = data[0]
    ma.plot([ydata, xdata])
    
def printlong(arr):
    for a in arr:
        if abs(a) < 1:
            print a
    
proto = wave([4.0, 6.0, 2.0, 10.0, 8.0, 8.0, 6.0, 4.0], 3)
arr = proto.get_diffs(1)
print arr

# data = ma.openLV()
# plot(data)
# proto = wave(data[1], 1)
# proto.thresh(1)
# proto.reconstruct()
# plot([data[1], proto.arr])
# printlong(arr)
