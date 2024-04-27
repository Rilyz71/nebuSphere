import pyautogui
import time
import pygetwindow as gw


def pixel_match():
    expected_color = (60, 45, 48)

    x, y = 2127, 374

    if pyautogui.pixelMatchesColor(x, y, expected_color):
        print("Цвет пикселя совпадает с ожидаемым!!")
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
    else:
        print("Цвет пикселя не совпадает с ожидаемым.(")


def get_all_windows():
    """
    Выводит список названий всех открытых окон
    :return: all_windows
    """
    all_windows = gw.getAllWindows()

    for window in all_windows:
        print(window.title)
    return all_windows


if __name__ == "__main__":
    pixel_match()
