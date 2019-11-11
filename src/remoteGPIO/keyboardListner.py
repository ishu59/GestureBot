# import os,sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from pynput.keyboard import Key, Listener
from src.remoteGPIO.led import light_off, light_on

def on_press(key):
    print('{0} pressed'.format(key))
    light_on()
    #
    # if key == 'a':
    #     light_on()www
    # elif key == Key.up:
    #     light_on()

def on_release(key):
    print('{0} release'.format(key))
    light_off()
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()