import pyautogui as pg
import keyboard as kb
from PIL import Image, ImageGrab
import time
import math

def get_pixel(img, x, y):
    px = img.load()
    return px[x, y]

#to obtain background colour at that instant
def get_bg_color(img):
    return img.getpixel((0, 0))

def main():
    x = 0
    y = 135
    width = 1920
    height = 875

    lst_jump_time = 0
    curr_jump_time = 0
    lst_int_time = 0

    obs_top, obs_bottom, x_start_obs, x_end_obs = 557, 486, 230, 390
    bird_y = 460

    #delay to switch to chrome
    time.sleep(3)

    while True:
        #STOP keys for the program
        if kb.is_pressed('q') or kb.is_pressed('esc'):
            break
        
        scshot = pg.screenshot(region=(x, y, width, height))
        bg_color = get_bg_color(scshot)

        #detecting objstacles
        for i in range(x_start_obs, x_end_obs):
            if get_pixel(scshot, i, obs_top) != bg_color or get_pixel(scshot, i, obs_bottom) != bg_color:
                kb.press('up')
                curr_jump_time = time.time()
                break

            if get_pixel(scshot, i, bird_y) != bg_color:
                kb.press("down")
                time.sleep(0.4)
                kb.release("down")
                break

        int_time = curr_jump_time - lst_jump_time

        #checking for acceleration
        if lst_int_time != 0 and math.floor(int_time) != math.floor(lst_int_time):
            x_end_obs += 4
            if x_end_obs >= width:
                x_end_obs = width

        lst_jump_time = curr_jump_time
        lst_int_time = int_time

if __name__ == "__main__":
    main()
