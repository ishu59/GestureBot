from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

class LedTrigger:
    def __init__(self, host=None):
        self.pin_led = 18
        self.factory = None
        if host is not None:
            self.factory = PiGPIOFactory(host=host)
        if self.factory is not None:
            self.led = LED(self.pin_led, pin_factory=self.factory)
        else:
            self.led = LED(self.pin_led)
    def light_on(self):
        self.led.on()
    def light_off(self):
        self.led.off()




    # # remote
    # red = LED(18, pin_factory=factory)
    # # local
    # # red = LED(18)
    # while True:
    #     red.on()
    #     sleep(1)
    #     red.off()
    #     sleep(1)

    #

    # Example for PWM
    # led = PWMLED(18, pin_factory=factory)
    # for b in range(100):
    #     led.value = b / 100
    #     sleep(0.1)
    # led.value = 0