from time import sleep
import RPi.GPIO as GPIO

# TODO: Define you device name
piName = None

# DEFINE PINS
lightPin = 4
buttonPin = 17

# SETUP BREADBOARD
# The GPIO.BCM option means that you are referring to the pins by the "Broadcom SOC channel" number,
# as you can see on breadboard printed schema
GPIO.setmode(GPIO.BCM)

# tell the system the an LED pin will be an output (we will send data there)
GPIO.setup(lightPin, GPIO.OUT)

# tell the system the an BUTTON pin will be an input (we will receive data from there)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# DEFINE VARIABLEs
# response values for button from a breadboard
buttonIsPressed = 0
buttonIsReleased = 1
# request values for LED on a breadboard
lightIsOn = 1
lightIsOff = 0

# this while cycle infinitely checks the state of a button on the breadboard every 0.1 seconds (100 milliseconds)
# and send updated data to a breadboard
while True:
    # initialize ledState variable 
    ledState = lightIsOff

    # read the current button state from breadboard
    currentButtonState = GPIO.input(buttonPin)

    ####### TODO area: 
    # STEP 1: Implement logic for these requirements:
    # 1. When the button is pressed - set the light on.
    # 2. When the button is not pressed - set the light off.
    if currentButtonState == buttonIsPressed:
        print ("Button Pressed")
        ledState = lightIsOn
        
    # STEP 2: Implement logic to send the email:
    # 1. When the buttton is pressed - send an email about the problem.
    
    #######

    # send the state of the LED to breadbord, so it can turn a light on or off
    GPIO.output(lightPin, ledState)

    # this prevents code from running to fast and using too much resources
    # we stop everything for 0.01 seconds as humans can't press the button faster than 10 times per second
    sleep(.10)
