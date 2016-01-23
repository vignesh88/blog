# Import the GPIO and time libraries
import RPi.GPIO as GPIO
import time

#####Moorse code definition######
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
######End of moorse code definition######

# Set the pin designation type.
# In this case, we use BCM- the GPIO number- rather than the pin number itself.
GPIO.setmode (GPIO.BCM)

# So that you don't need to manage non-descriptive numbers,
# set "LIGHT" to 4 so that our code can easily reference the correct pin.
LIGHT = 4

# Because GPIO pins can act as either digital inputs or outputs,
# we need to designate which way we want to use a given pin.
# This allows us to use functions in the GPIO library in order to properly send and receive signals.
GPIO.setup(LIGHT,GPIO.OUT)


def dot():
        GPIO.output(LIGHT,True)
        time.sleep(0.2)
        GPIO.output(LIGHT,False)
        time.sleep(0.2)

def dash():
        GPIO.output(LIGHT,True)
        time.sleep(0.5)
        GPIO.output(LIGHT,False)
        time.sleep(0.2)

try:
    while True:
		input = raw_input('What would you like to send? ')
		for letter in input:
			for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dash()
				elif symbol == '.':
					dot()
				else:
					time.sleep(0.5)
			time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
