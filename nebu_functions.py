from const import *
from auxiliary import *
import pyautogui
from time import sleep


def after_death_tap_start(win_title):
    """
    Нажимает "Играть" сразу же после смерти игрока
    Для безопасности после клика ожидание = 2 секунды
    :return:
    """
    win_x, win_y = get_win_coords(win_title)

    x = win_x + X_KOEFF_1280_PLAYBUTTON
    y = win_y + Y_KOEFF_1280_PLAYBUTTON

    expected_color = (154, 7, 87)

    while True:
        if pyautogui.pixelMatchesColor(x, y, expected_color):
            pyautogui.click(x, y)
            sleep(2)
