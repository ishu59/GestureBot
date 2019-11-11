# from gpiozero import LED, Button
# from signal import pause
# from gpiozero.pins.pigpio import PiGPIOFactory
# import os
#
# os.environ["PIGPIO_ADDR"] = "10.0.0.160"
# os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"
#
# factory = PiGPIOFactory(host='10.0.0.160')
# # red = LED(17)
# led = LED(18, pin_factory=factory)
# button = Button(3)
#
# button.when_pressed = led.on
# button.when_released = led.off
#
# pause()