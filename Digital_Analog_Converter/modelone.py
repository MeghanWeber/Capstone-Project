from scipy import io
import numpy as np
import time
import sys
import math
import Adafruit_MCP4725

dac = Adafruit_MCP4725.MCP4725()
first_arg = sys.argv[1]

def modelone(intvalue = first_arg): #first_arg
    intvalue = int(intvalue)
    mat = io.loadmat('modelonescale.mat');
    y_value = mat['interpoalteddatay'];
    y_value = np.transpose(y_value);
    new_value = np.zeros(y_value.shape)

    for jj in range(len(y_value)):
        if y_value[jj] == 1:
            new_value[jj] = 3900
        elif y_value[jj] == 2:
            new_value[jj] = 3550
        elif y_value[jj] == 3:
            new_value[jj] = 3350
        elif y_value[jj] == 4:
            new_value[jj] = 3200
        elif y_value[jj] == 5:
            new_value[jj] = 2950
        elif y_value[jj] == 6:
            new_value[jj] = 2820
        elif y_value[jj] == 7:
            new_value[jj] = 2700
        elif y_value[jj] == 8:
            new_value[jj] = 2620
        elif y_value[jj] == 9:
            new_value[jj] = 2540
        elif y_value[jj] == 10:
            new_value[jj] = 2460
        elif y_value[jj] == 11:
            new_value[jj] = 2380
        elif y_value[jj] == 12:
            new_value[jj] = 2300
        elif y_value[jj] == 13:
            new_value[jj] = 2240
        elif y_value[jj] == 14:
            new_value[jj] = 2190
        elif y_value[jj] == 15:
            new_value[jj] = 2145
        elif y_value[jj] == 16:
            new_value[jj] = 2100
        elif y_value[jj] == 17:
            new_value[jj] = 2055
        elif y_value[jj] == 18:
            new_value[jj] = 2020
        elif y_value[jj] == 19:
            new_value[jj] = 1985
        elif y_value[jj] == 20:
            new_value[jj] = 1950
        elif y_value[jj] == 21:
            new_value[jj] = 1920
        elif y_value[jj] == 22:
            new_value[jj] = 1894
        elif y_value[jj] == 23:
            new_value[jj] = 1870
        elif y_value[jj] == 24:
            new_value[jj] = 1848
        elif y_value[jj] == 25:
            new_value[jj] = 1828
        elif y_value[jj] == 26:
            new_value[jj] = 1811
        elif y_value[jj] == 27:
            new_value[jj] = 1794
        elif y_value[jj] == 28:
            new_value[jj] = 1779
        elif y_value[jj] == 29:
            new_value[jj] = 1764
        elif y_value[jj] == 30:
            new_value[jj] = 1751
        elif y_value[jj] == 31:
            new_value[jj] = 1735
           
    
    
    var = 1;
    
    X = math.exp(-(intvalue+193.74)/54.91)
    new_value = new_value.flatten()
    while var == 1:
        for val in new_value:
            val = int(val)
            dac.set_voltage(val)
            time.sleep(X)
if __name__ == "__main__":
    modelone()

