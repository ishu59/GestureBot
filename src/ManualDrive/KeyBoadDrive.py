import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

# from Bot.BasicBot import BasicBot
from Bot.BasicBotLocal import BasicBotLocal
from pynput.keyboard import Key, Listener
bot_ip_address = '10.0.0.195'
# os.environ["PIGPIO_ADDR"] = bot_ip_address
# os.environ["GPIOZERO_PIN_FACTORY"] = "pigpio"

# bot = BasicBot(host=bot_ip_address)
bot = BasicBotLocal()
def on_press(key):
    print('{0} pressed'.format(key))
    if key == 'w' or key == Key.up:
        bot.run()
    elif key == 's' or key == Key.down:
        bot.back()
    elif key == 'a' or key == Key.left:
        bot.left()
    elif key == 'd' or key == Key.right:
        bot.right()
    elif key == 'e' or key == Key.space:
        # print('Led start')
        # bot.start_test_led()
        bot.whistle()
    else:
        # print('Led start')
        # bot.start_test_led()
        bot.brake()

def on_release(key):
    print('{0} release'.format(key))
    bot.brake()
    # bot.stop_test_led()

    if key == Key.esc:
        # Stop listener
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()