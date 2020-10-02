import sys
from Brightness.ControlBrightness import setBrightness

# Control brightness
# -b incr | decr

if __name__ == "__main__":
    args = sys.argv
    if args[1] == '-b':
        setBrightness(args[2])
    else:
        print('Error')
