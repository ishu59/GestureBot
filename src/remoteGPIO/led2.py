import os
from time import sleep
from pprint import pprint
os.environ["PIGPIO_ADDR"] = "10.0.0.160"
os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"
# pprint(os.environ)
from gpiozero import LED

gpio_pin = 18   #we are using gpio 26
led = LED(gpio_pin)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)