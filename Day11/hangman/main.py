import pygame as py
import os

py.init()
screen = py.display.set_mode((600, 600))
bg_img = py.image.load(os.path.join("img", "2.png"))
bg_img = py.transform.scale(bg_img, (600, 600))
runing = True

while runing:
    screen.blit(bg_img,(0,0))
    for event in py.event.get():
        if event.type == py.QUIT:
            runing = False
    py.display.update()

py.quit()