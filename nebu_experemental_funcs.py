from const import *
from auxiliary import *
import pyautogui
from time import sleep


def move_and_click_to_plasmashop(win_title):
    x_koeff = X_KOEFF_1280_SHOP
    y_koeff = Y_KOEFF_1280_SHOP
    x_win, y_win = get_win_coords(win_title)

    x, y = x_win + x_koeff, y_win + y_koeff
    pyautogui.moveTo(x, y, duration=DURATION)
    sleep(0.5)
    pyautogui.click(x, y)


def experemental_sphere():
    win_x, win_y = get_win_coords("Карась")
    region = (win_x, win_y, 1430, 810)
    target_color = (86, 138, 206)

    screenshot = pyautogui.screenshot(region=region)
    while True:
        for x in range(region[2]):
            for y in range(region[3]):
                pixel_color = screenshot.getpixel((x, y))

                if pixel_color == target_color:
                    pyautogui.click(win_x + x, win_y + y)
                    pyautogui.mouseDown()
                    pyautogui.press("w")
                    sleep(1.5)
                    pyautogui.mouseUp()
                    screenshot = pyautogui.screenshot(region=region)