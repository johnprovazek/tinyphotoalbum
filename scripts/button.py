# button 1 - D23
# button 2 = D26
# button 3 = D6
# button 4 = D5

import digitalio
import board
from adafruit_debouncer import Debouncer

button_1_input = digitalio.DigitalInOut(board.D23)
button_1_input.switch_to_input(pull=digitalio.Pull.UP)
button_1 = Debouncer(button_1_input)

button_2_input = digitalio.DigitalInOut(board.D26)
button_2_input.switch_to_input(pull=digitalio.Pull.UP)
button_2 = Debouncer(button_2_input)

button_3_input = digitalio.DigitalInOut(board.D6)
button_3_input.switch_to_input(pull=digitalio.Pull.UP)
button_3 = Debouncer(button_3_input)

button_4_input = digitalio.DigitalInOut(board.D5)
button_4_input.switch_to_input(pull=digitalio.Pull.UP)
button_4 = Debouncer(button_4_input)

while True:
    button_1.update()
    button_2.update()
    button_3.update()
    button_4.update()
    if button_1.fell:
        print("button_1: pressed")
#     if button_1.rose:
#         print("button_1: released")
    if button_2.fell:
        print("button_2: pressed")
#     if button_2.rose:
#         print("button_2: released")
    if button_3.fell:
        print("button_3: pressed")
#     if button_3.rose:
#         print("button_3: released")
    if button_4.fell:
        print("button_4: pressed")
#     if button_4.rose:
#         print("button_4: released")
    