from Bot import BasicBot

class BotAdvance(BasicBot):
    pass
    # Motor pins are initialized into output mode
    # Key pin is initialized into input mode
    # Ultrasonic pin,RGB pin,servo pin initialization
    def __init__(self):
        # Definition of RGB module pins
        self.EchoPin = 0
        self.TrigPin = 1

        # Definition of RGB module pins
        self.LED_R = 22
        self.LED_G = 27
        self.LED_B = 24

        # Definition of servo pin
        self.ServoPin = 23

        # Definition of outfire pin
        # self.OutfirePin = 2

        # #TODO Distance sensor and led not configured, please work on it later
        # #todo need to use DistanceSensor, PWMLed class for this, check api at
        # #todo https://gpiozero.readthedocs.io/en/stable/api_input.html
        # GPIO.setup(EchoPin, GPIO.IN)
        # GPIO.setup(TrigPin, GPIO.OUT)
        # GPIO.setup(LED_R, GPIO.OUT)
        # GPIO.setup(LED_G, GPIO.OUT)
        # GPIO.setup(LED_B, GPIO.OUT)
        # GPIO.setup(ServoPin, GPIO.OUT)

        # Set the PWM pin and frequency is 2000hz
        # pwm_ENA = GPIO.PWM(ENA, 2000)
        # pwm_ENB = GPIO.PWM(ENB, 2000)
        # pwm_ENA.start(0)
        # pwm_ENB.start(0)
        #
        # pwm_servo = GPIO.PWM(ServoPin, 50)
        # pwm_servo.start(0)
        # pwm_rled = GPIO.PWM(LED_R, 1000)
        # pwm_gled = GPIO.PWM(LED_G, 1000)
        # pwm_bled = GPIO.PWM(LED_B, 1000)
        # pwm_rled.start(0)
        # pwm_gled.start(0)
        # pwm_bled.start(0)


    # #TODO need to implement ultrasonic depth detection
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
    # #TODO Need to implement servo for depth sensor
    # # The servo rotates to the specified angle
    # def servo_appointed_detection(pos):
    #     for i in range(18):
    #         pwm_servo.ChangeDutyCycle(2.5 + 10 * pos / 180)
    #

    # #TODO need to implement code for LED output
    # # Color_LED light the specified color
    # def color_led_pwm(iRed, iGreen, iBlue):
    #     print(iRed)
    #     print(iGreen)
    #     print(iBlue)
    #     v_red = (100 * iRed) / 255
    #     v_green = (100 * iGreen) / 255
    #     v_blue = (100 * iBlue) / 255
    #     print(v_red)
    #     print(v_green)
    #     print(v_blue)
    #     pwm_rled.ChangeDutyCycle(v_red)
    #     pwm_gled.ChangeDutyCycle(v_green)
    #     pwm_bled.ChangeDutyCycle(v_blue)
    #     time.sleep(0.02)
