from PIL import Image
from os import environ, listdir
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def check_file(path):
    try:
        Image.open(path)
    except IOError:
        print("File is not an image.")
        pygame.quit()
        exit()


print("ASCII Art Algorithm by Valiant#4075.")
pygame.init()

filename = "picture/" + listdir("picture")[0]  # find first file in picture directory
check_file(filename)
raw_image = Image.open(filename)
white = (255, 255, 255)
black = (0, 0, 0)
# characters used for simulating pixel brightness levels, dark to bright
characters = [" ", ".", ",", "~", "=", "{", "%", "&", "@"]
size = raw_image.size  # raw_image later converts to thumbnail, we need original size for resizing showcase image
showcase_image = raw_image.resize(size, Image.NEAREST)
showcase_image.show()
# resize with aspect ratio (max dimensions 128x72) and then convert to grayscale (mode L)
raw_image.thumbnail((128, 72), Image.BILINEAR)

showcase_image_grayscale = raw_image.resize(size, Image.NEAREST).convert("L")
showcase_image_grayscale.show()
image = raw_image.convert("L")

display = pygame.display.set_mode((raw_image.width * 10, raw_image.height * 10))
pygame.display.set_caption("ASCII Image")
font = pygame.font.SysFont("consolas", 13)

on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
    display.fill(black)
    for x in range(raw_image.width):
        for y in range(raw_image.height):
            brightness = round(image.getpixel((x, y))/32)
            char = characters[brightness]
            text = font.render(char, True, white)
            display.blit(text, (x * 10, y * 10))
    pygame.display.update()
pygame.quit()
