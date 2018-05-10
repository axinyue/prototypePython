import random
from PIL import Image,ImageFont,ImageDraw
from send_msg_code import rand_code


class VerifyingCode(object):
    def __init__(self):
        self.font_path = "font.ttf"
        self.size = (127,53)
        self.bgcolor = (255,255,255)
        pass

    def gene_code(self):
        width,height = self.size

        image = Image.new("RGBA",(width,height))
        font = ImageFont.truetype(self.font_path,40)
        draw = ImageDraw.Draw(image)
        font_width,font_height = font.getsize()
        text =rand_code()
        draw.text(0,0,text,fill=self.bgcolor)


