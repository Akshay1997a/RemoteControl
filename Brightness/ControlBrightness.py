import os
import platform

INCR = 'incr'
DECR = 'decr'

MAX_BRIGHTNESS = 937
MIN_BRIGHTNESS = 9

#[20 * 1,20 * 2,20 * 3,20 * 4,20 * 5 + 12]
#mean * i + min

#[194, 380, 565, 751, 937]


def setBrightness(flag):
    if flag == INCR:
        print('Increase Brightness')
    
    else:
        print('Decress Brightness')
        
