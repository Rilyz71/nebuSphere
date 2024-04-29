from nebuSphere import auxiliary
import pyautogui
from time import sleep
from nebuSphere.data import coefficients


def move_and_click_to_plasmashop(win_title):
    x_koeff = coefficients.X_COEFF_1280_SHOP
    y_koeff = coefficients.Y_COEFF_1280_SHOP
    x_win, y_win = auxiliary.get_win_coords(win_title)

    x, y = x_win + x_koeff, y_win + y_koeff
    pyautogui.moveTo(x, y, duration=coefficients.DURATION)
    sleep(0.5)
    pyautogui.click(x, y)
