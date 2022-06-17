#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Cicuit is 3.3 V to resistor to led to gnd. The gnd is assigned to 
# GPIO17. Since 3.3 V is the source, that is the HIGH. In order to
# create a voltage difference, the gnd must be different from 3.3V,
# so we set GPIO17 to LOW (meaning 0V), thus creating a potential
# difference and thus we have a live circuit. 

LedPin = 17

def setup():
  # Set the GPIO modes to BCM Numbering
  GPIO.setmode(GPIO.BCM)

  # Set LedPin's mode to output,and initial level to High(3.3v)
  GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a main function for main process
def main():
  while True:
    print ('...LED ON')
    # Turn on LED
    GPIO.output(LedPin, GPIO.LOW) #gnd set to 0V
    time.sleep(0.5)
    print ('LED OFF...')
    # Turn off LED
    GPIO.output(LedPin, GPIO.HIGH)    #gnd set to 3.3V
    time.sleep(0.5)

# Define a destroy function for clean up everything after the script finished
def destroy():
  # Turn off LED
  GPIO.output(LedPin, GPIO.HIGH)   #shut off the led by setting gnd to 3.3V
  # Release resource
  GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
  setup()
  try:
    main()
    # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    except KeyboardInterrupt:
      destroy()
