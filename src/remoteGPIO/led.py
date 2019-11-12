from gpiozero import LED, PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
factory = PiGPIOFactory(host='10.0.0.160')

# remote
red = LED(18, pin_factory=factory)
# local
# red = LED(18)
while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

# def light_on():
#     red.on()
#
# def light_off():
#     red.off()
#

 # Example for PWM
# led = PWMLED(18, pin_factory=factory)
# for b in range(100):
#     led.value = b / 100
#     sleep(0.1)
# led.value = 0