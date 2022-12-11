# script to generate sample date photos in same resolution as gameboy camera

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_image(month, day):
    date_text = month + "_" + day
    width = 128
    height = 112
    left = [(0, 0), (0, 111)]
    right = [(127, 0), (127, 111)]
    top = [(0, 0), (127, 0)] #done
    bottom = [(0, 111), (127, 111)] #done
    square1 = [(1, 80), (31, 110)]
    square2 = [(32, 80), (63, 110)]
    square3 = [(64, 80), (95, 110)]
    square4 = [(96, 80), (126, 110)]
    fnt = ImageFont.truetype("../fonts/Cascadia.ttf", 40)
    img  = Image.new( mode = "RGB", size = (width, height) )
    ImageDraw.Draw(img).line(top, fill="white", width = 0)
    ImageDraw.Draw(img).line(bottom, fill="yellow", width = 0)
    ImageDraw.Draw(img).line(left, fill="blue", width = 0)
    ImageDraw.Draw(img).line(right, fill="red", width = 0)
    ImageDraw.Draw(img).rectangle(square1, fill =(255,255,255))
    ImageDraw.Draw(img).rectangle(square2, fill =(170,170,170))
    ImageDraw.Draw(img).rectangle(square3, fill =(85,85,85))
    ImageDraw.Draw(img).rectangle(square4, fill =(0,0,0))
    ImageDraw.Draw(img).text((5, 30),date_text, font=fnt, fill=(0, 255, 0))
    img.save("../photos/date_photos/" + month + "_" + day + ".png")


years = ['2024']
months = ['1', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', '11', '12']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(years)):
    for j in range(len(months)):
        if (((int(years[i]) % 4 == 0 and int(years[i]) % 100 != 0) or (int(years[i])% 400 == 0)) and months[j] == '2'):
            for k in range(1, days[j] + 2):
                create_image(months[j], str(k))

        else:
            for k in range(1, days[j] + 1):
                create_image(months[j], str(k))




