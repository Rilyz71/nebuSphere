from nebuSphere.data.coefficients import *
from nebuSphere.auxiliary import *
import pyautogui
from time import sleep


def move_and_click_to_plasmashop(win_title):
    x_koeff = X_COEFF_1280_SHOP
    y_koeff = Y_COEFF_1280_SHOP
    x_win, y_win = get_win_coords(win_title)

    x, y = x_win + x_koeff, y_win + y_koeff
    pyautogui.moveTo(x, y, duration=DURATION)
    sleep(0.5)
    pyautogui.click(x, y)
