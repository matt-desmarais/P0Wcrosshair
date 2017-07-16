import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO 24, 23 & 18 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# threaded callbacks to run in new thread when button events are detected
def topbutton(channel):
    print "Top Button Pressed"

def ctrbutton(channel):
    print "Center Button Pressed"

def lowbutton(channel):
    print "Lower Button Pressed"

print "Make sure buttons are connected to GPIO 24, 23 and 18 (and each to GND)!"
raw_input("Press Enter when ready\n>")

GPIO.add_event_detect(24, GPIO.FALLING, callback=topbutton, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, callback=ctrbutton, bouncetime=300)
GPIO.add_event_detect(18, GPIO.FALLING, callback=lowbutton, bouncetime=300)

while True:
    time.sleep(1)

GPIO.cleanup()           # clean up GPIO on normal exit
