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
    mean = (MAX_BRIGHTNESS - MIN_BRIGHTNESS) / 5
    ar = [int((mean * x) + MIN_BRIGHTNESS) for x in range(1, 6)]
    if flag == INCR:
        print('Increase Brightness')
        ls = os.listdir('/sys/class/backlight')
        for i in ls:
            bright = open('/sys/class/backlight/'+i+'/brightness', "w+")
            currentValue = int(bright.read())
            value = currentValue
            for i in range(len(ar)):
                if currentValue % ar[i] == currentValue:
                    value = ar[i]
                    break
            print(currentValue, value)
            if value <= MAX_BRIGHTNESS:
                bright.write(str(value))
            bright.close()
    else:
        print('Decress Brightness')
        ls = os.listdir('/sys/class/backlight')
        for i in ls:
            bright = open('/sys/class/backlight/'+i+'/brightness', "w+")
            currentValue = int(bright.read())
            value = currentValue
            for i in range(len(ar)):
                if currentValue % ar[i] != currentValue:
                    value = ar[i]
                    break
            print(currentValue, value)
            if value >= MIN_BRIGHTNESS:
                bright.write(str(value))
            bright.close()
