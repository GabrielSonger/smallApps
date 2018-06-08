from PIL import Image, ImageDraw, ImageFont
from os import path


class ImageWatermark(object):
    def __init__(self, input_img):
        self.image = Image.open(input_img)

    def set_font(self, size, font ='FreeMono.ttf'):
        font_file = path.join(path.dirname(path.realpath(__file__)), font)
        fonta = ImageFont.truetype(font_file, size)
        return fonta

    def set_color(self, color):
        return color

    def add_watermark(self, text, pos, font, color):
        drawing = ImageDraw.Draw(self.image)
        drawing.text(pos, text, fill=color, font=font)
        self.image.show()
        self.image.save('cat.jpg')


if __name__ == '__main__':
    image = ImageWatermark('me.jpg')
    font = image.set_font(40)
    color = image.set_color((3, 8, 12))
    text = 'Hello World'
    pos = (0, 0)
    image.add_watermark(text, pos, font, color)

