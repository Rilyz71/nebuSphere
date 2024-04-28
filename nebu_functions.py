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


def antioffline(win_title: str):
    target_color = (115, 175, 170)

    # + Отслеживание положения окна каждый 1.5 сек
    while True:
        win_x, win_y = get_win_coords(win_title)
        x = win_x + X_KOEFF_1280_ANTIOFF_SIGH
        y = win_y + Y_KOEFF_1280_ANTIOFF_SIGH
        pixel = pyautogui.pixelMatchesColor(x, y, target_color)

        print(f"Checked - {x}, {y}")

        if pixel:
            pyautogui.click(x, y)
        sleep(1.5)
