import os
import time
from gpiozero import LED, PWMLED, Buzzer, Motor
import string
import serial
import socket

from gpiozero.pins.pigpio import PiGPIOFactory

# os.environ["PIGPIO_ADDR"] = "10.0.0.160"
# os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"

# Definition of  key value
class BasicBotLocal:

    # Motor pins are initialized into output mode
    # Key pin is initialized into input mode
    # Ultrasonic pin,RGB pin,servo pin initialization
    def __init__(self):
        # Definition of  motor pins
        # self.factory = PiGPIOFactory(host=host)
        self.IN1 = 20
        self.IN2 = 21
        self.IN3 = 19
        self.IN4 = 26
        self.ENA = 16
        self.ENB = 13
        self.CarSpeedControl = 0.1
        # Definition of RGB module pins
        self.EchoPin = 0
        self.TrigPin = 1

        # Definition of RGB module pins
        self.LED_R = 22
        self.LED_G = 27
        self.LED_B = 24

        # Definition of servo pin
        self.ServoPin = 23

        # Definition of buzzer pin
        self.buzzer_pin = 8

        # Definition of outfire pin
        # self.OutfirePin = 2

        # #todo Important Look at ENA_pin, ENB_pin for pulse width modulation
        # ENA_pin_out = LED(ENA, initial_value=True)
        # IN1_pin_out = LED(IN1, initial_value=False)
        # IN2_pin_out = LED(IN2, initial_value=False)
        # Replaced led pins with MotorClass
        self.motor_a: Motor = Motor(forward=self.IN1, backward=self.IN2, enable=self.ENA)


        # ENB_pin_out = LED(ENB, initial_value=True)
        # IN3_pin_out = LED(IN3, initial_value=False)
        # IN4_pin_out = LED(IN4, initial_value=False)
        self.motor_b: Motor = Motor(forward=self.IN3, backward=self.IN4, enable=self.ENB)
        # GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
        # GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
        # GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
        # GPIO.setup(ENB, GPIO.OUT, initial=GPIO.HIGH)
        # GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
        # GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)


        # GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.HIGH)
        # buzzer_pin_out = LED(buzzer, initial_value=True)
        self.buzzer: Buzzer = Buzzer(pin=self.buzzer_pin)
        self.buzzer.blink()

        # self.test_led_pin = 18
        # self.test_led = LED(pin=self.test_led_pin)


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
        # GPIO.output(IN1, GPIO.HIGH)
        # GPIO.output(IN2, GPIO.LOW)
        # GPIO.output(IN3, GPIO.HIGH)
        # GPIO.output(IN4, GPIO.LOW)
        # pwm_ENA.ChangeDutyCycle(CarSpeedControl)
        # pwm_ENB.ChangeDutyCycle(CarSpeedControl)
        self.motor_a.forward()
        self.motor_b.forward()

    # back
    def back(self):
        self.motor_a.backward()
        self.motor_b.backward()
        # GPIO.output(IN1, GPIO.LOW)
        # GPIO.output(IN2, GPIO.HIGH)
        # GPIO.output(IN3, GPIO.LOW)
        # GPIO.output(IN4, GPIO.HIGH)
        # pwm_ENA.ChangeDutyCycle(CarSpeedControl)
        # pwm_ENB.ChangeDutyCycle(CarSpeedControl)


    # trun left
    def left(self):
        self.motor_a.stop()
        self.motor_b.forward()
        # GPIO.output(IN1, GPIO.LOW)
        # GPIO.output(IN2, GPIO.LOW)
        # GPIO.output(IN3, GPIO.HIGH)
        # GPIO.output(IN4, GPIO.LOW)
        # pwm_ENA.ChangeDutyCycle(CarSpeedControl)
        # pwm_ENB.ChangeDutyCycle(CarSpeedControl)


    # turn right
    def right(self):
        self.motor_a.forward()
        self.motor_b.stop()
        # GPIO.output(IN1, GPIO.HIGH)
        # GPIO.output(IN2, GPIO.LOW)
        # GPIO.output(IN3, GPIO.LOW)
        # GPIO.output(IN4, GPIO.LOW)
        # pwm_ENA.ChangeDutyCycle(CarSpeedControl)
        # pwm_ENB.ChangeDutyCycle(CarSpeedControl)


    # turn left in place
    def spin_left(self):
        self.motor_a.backward()
        self.motor_b.forward()
        # GPIO.output(IN1, GPIO.LOW)
        # GPIO.output(IN2, GPIO.HIGH)
        # GPIO.output(IN3, GPIO.HIGH)
        # GPIO.output(IN4, GPIO.LOW)
        # pwm_ENA.ChangeDutyCycle(CarSpeedControl)
        # pwm_ENB.ChangeDutyCycle(CarSpeedControl)


    # turn right in place
    def spin_right(self):
        self.motor_a.forward()
        self.motor_b.backward()
        # GPIO.output(IN1, GPIO.HIGH)
        # GPIO.output(IN2, GPIO.LOW)
        # GPIO.output(IN3, GPIO.LOW)
        # GPIO.output(IN4, GPIO.HIGH)
        # pwm_ENA.ChangeDutyCycle(CarSpeedControl)
        # pwm_ENB.ChangeDutyCycle(CarSpeedControl)


    # brake
    def brake(self):
        self.motor_a.stop()
        self.motor_b.stop()
        # GPIO.output(IN1, GPIO.LOW)
        # GPIO.output(IN2, GPIO.LOW)
        # GPIO.output(IN3, GPIO.LOW)
        # GPIO.output(IN4, GPIO.LOW)


    # # Ultrasonic function
    # def Distance_test():
    #     GPIO.output(TrigPin, GPIO.HIGH)
    #     time.sleep(0.000015)
    #     GPIO.output(TrigPin, GPIO.LOW)
    #     while not GPIO.input(EchoPin):
    #         pass
    #         t1 = time.time()
    #     while GPIO.input(EchoPin):
    #         pass
    #         t2 = time.time()
    #     print(("distance is %d " % (((t2 - t1) * 340 / 2) * 100)))
    #     time.sleep(0.01)
    #     return ((t2 - t1) * 340 / 2) * 100
    #

    # # The servo rotates to the specified angle
    # def servo_appointed_detection(pos):
    #     for i in range(18):
    #         pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)
    #

    # whistle
    def whistle(self):
        self.buzzer.blink()
        # GPIO.output(buzzer, GPIO.LOW)
        # time.sleep(0.1)
        # GPIO.output(buzzer, GPIO.HIGH)
        # time.sleep(0.001)