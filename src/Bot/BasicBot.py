import os
import time
from gpiozero import LED, PWMLED, Buzzer, Motor
import string
import serial
import socket
from gpiozero.pins.pigpio import PiGPIOFactory

bot_ip_address = '10.0.0.195'
os.environ["PIGPIO_ADDR"] = bot_ip_address
os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"

# Definition of  key value
class BasicBot:

    # Motor pins are initialized into output mode
    # Key pin is initialized into input mode
    # Ultrasonic pin,RGB pin,servo pin initialization
    def __init__(self, host=None):
        # Definition of  motor pins
        self.factory = None
        if host is not None:
            self.factory = PiGPIOFactory(host=host)
        self.IN1 = 20
        self.IN2 = 21
        self.IN3 = 19
        self.IN4 = 26
        self.ENA = 16
        self.ENB = 13
        self.CarSpeedControl = 0.2

        # Definition of buzzer pin
        self.buzzer_pin = 8
        if self.factory is not None:
            self.motor_a: Motor = Motor(forward=self.IN1, backward=self.IN2, enable=self.ENA, pwm=True, pin_factory=self.factory)
            self.motor_b: Motor = Motor(forward=self.IN3, backward=self.IN4, enable=self.ENB, pwm=True, pin_factory=self.factory)
            # self.buzzer: Buzzer = Buzzer(pin=self.buzzer_pin, pin_factory=self.factory)
            # self.buzzer.blink(on_time= 0.5, off_time=0.5 ,n=1)
            # self.buzzer.off()
        else:
            self.motor_a: Motor = Motor(forward=self.IN1, backward=self.IN2, enable=self.ENA, pwm=True)
            self.motor_b: Motor = Motor(forward=self.IN3, backward=self.IN4, enable=self.ENB, pwm=True)
            # self.buzzer: Buzzer = Buzzer(pin=self.buzzer_pin)
            #self.buzzer.blink(on_time=0.5, off_time=0.5, n=1)


    #     self.test_led_pin = 18
    #     self.test_led = LED(pin=self.test_led_pin, pin_factory=self.factory)
    #
    #
    # def blink_test_led(self):
    #     self.test_led.blink(n=5)
    #
    # def start_test_led(self):
    #     self.test_led.on()
    #
    # def stop_test_led(self):
    #     self.test_led.off()

    # Advance
    def run(self):
        self.motor_a.forward(self.CarSpeedControl)
        self.motor_b.forward(self.CarSpeedControl)

    # back
    def back(self):
        self.motor_a.backward(self.CarSpeedControl)
        self.motor_b.backward(self.CarSpeedControl)

    # trun left
    def left(self):
        self.motor_a.stop()
        self.motor_b.forward(self.CarSpeedControl)

    # turn right
    def right(self):
        self.motor_a.forward(self.CarSpeedControl)
        self.motor_b.stop()

    # turn left in place
    def spin_left(self):
        self.motor_a.backward(self.CarSpeedControl)
        self.motor_b.forward(self.CarSpeedControl)

    # turn right in place
    def spin_right(self):
        self.motor_a.forward(self.CarSpeedControl)
        self.motor_b.backward(self.CarSpeedControl)

    # brake
    def brake(self):
        self.motor_a.stop()
        self.motor_b.stop()

    # whistle
    def whistle(self):
        pass
        # self.buzzer.blink(on_time= 0.5, off_time=0.5 ,n=1)
