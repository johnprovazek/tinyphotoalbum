import digitalio
import board
from PIL import Image, ImageDraw
from adafruit_rgb_display import st7735  # pylint: disable=unused-import
from adafruit_debouncer import Debouncer
import datetime
import pathlib
import random

width = 128
height = 128

def draw_from_path(image_path):
    screen_image = Image.new("RGB", (width,height))
    draw = ImageDraw.Draw(screen_image)
    draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 255))
    disp.image(screen_image)
    gb_photo = Image.open(image_path)
    Image.Image.paste(screen_image, gb_photo, (0, 8))
    disp.image(screen_image)

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the display:
disp = st7735.ST7735R(
    spi,
    rotation=270,
    width=128,
    height=128,
    x_offset=2,
    y_offset=3,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE 
)

# Button Setup
mode_button_input = digitalio.DigitalInOut(board.D23)
mode_button_input.switch_to_input(pull=digitalio.Pull.UP)
mode_button = Debouncer(mode_button_input)

toggle_button_input = digitalio.DigitalInOut(board.D26)
toggle_button_input.switch_to_input(pull=digitalio.Pull.UP)
toggle_button = Debouncer(toggle_button_input)

color_button_input = digitalio.DigitalInOut(board.D6)
color_button_input.switch_to_input(pull=digitalio.Pull.UP)
color_button = Debouncer(color_button_input)

brightness_button_input = digitalio.DigitalInOut(board.D5)
brightness_button_input.switch_to_input(pull=digitalio.Pull.UP)
brightness_button = Debouncer(brightness_button_input)

# Modes:
# 0: date mode - displays GB Camera photo on the current date. change photo at midnight.
# 1: slide-show mode - displays a random GB Camera photo. Use toggle button to adjust frequency.
mode = 0

# Frequency:
# 0: every 10 seconds
# 1: every 1 minutes
# 2: every 5 minutes
# 3: every 30 minutes
# 4: every 1 hour
frequency = 0

# Color:
# 0: greyscale
# 1: yellow
# 2: green
# 3: bricknose
color = 0

# Brightness:
# 0: 0% brightness
# 1: 25% brightness
# 2: 50% brightness
# 3: 75% brightness
# 4: 100% brightness
brightness = 4

# Time Handing
date_time_start = datetime.datetime.now()
date_day = date_time_start.day
date_formatted = str(date_time_start.month) + "_" + str(date_time_start.day)
last_randomized_time = date_time_start

# set image to start
draw_from_path("../photos/date_photos/" + date_formatted + ".png")


num_rand_photos = 0
for path in pathlib.Path("../photos/test_photos").iterdir():
    if path.is_file():
        num_rand_photos += 1

while True:
    # Check for updates from buttons
    mode_button.update()
    toggle_button.update()
    color_button.update()
    brightness_button.update()
    
    # Parse button inputs
    if mode_button.fell:
        mode = (mode + 1)%2
        if mode == 0:
            draw_from_path("../photos/date_photos/" + date_formatted + ".png")
        if mode == 1:
            random_num = random.randint(1, num_rand_photos)
            draw_from_path("../photos/test_photos/" + str(random_num) + ".png")
    if toggle_button.fell:
        if mode == 1:
            frequency = (frequency + 1)%5
            print(frequency)
    if color_button.fell:
        color = (color + 1)%4
        print(color)
        # change the color
    if brightness_button.fell:
        brightness = (brightness + 1)%5
        print(brightness)
        #change the brightness
        
    #date mode
    if mode == 0:
        cur_time = datetime.datetime.now()
        cur_day = cur_time.day
        if(cur_day != date_day):
            date_day = cur_day
            date_formatted = str(cur_time.month) + "_" + str(cur_time.day)
            draw_from_path("../photos/date_photos/" + date_formatted + ".png")
        
    #slide-show mode
    if mode == 1:
        cur_time = datetime.datetime.now()
        difference = (cur_time - last_randomized_time).total_seconds()
        if (frequency == 0 and difference > 10) or (frequency == 1 and difference > 60) or (frequency == 2 and difference > 300) or (frequency == 3 and difference > 1800) or (frequency == 4 and difference > 3600):
            last_randomized_time = cur_time
            random_num = random.randint(1, num_rand_photos)
            draw_from_path("../photos/test_photos/" + str(random_num) + ".png")