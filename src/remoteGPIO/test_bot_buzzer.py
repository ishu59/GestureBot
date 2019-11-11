import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
from pynput.keyboard import Key, Listener
# from src.remoteGPIO.led import light_off, light_on
from gpiozero import Buzzer, LED
bot_ip_address = '10.0.0.195'
os.environ["PIGPIO_ADDR"] = bot_ip_address
os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"
bot_ip_address = '10.0.0.195'
factory = PiGPIOFactory(host=bot_ip_address)
# b = Buzzer(8,pin_factory=factory )
# b.blink()
# def on_press(key):
#     print('{0} pressed'.format(key))
#     b.beep()
#     #
#     # if key == 'a':
#     #     light_on()www
#     # elif key == Key.up:
#     #     light_on()
#
# def on_release(key):
#     print('{0} release'.format(key))
#     b.beep()
#     if key == Key.esc:
#         # Stop listener
#         return False
#
# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

red = LED(8, pin_factory=factory)
while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
