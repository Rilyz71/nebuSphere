import pyautogui
import time

X, Y = 2127, 371


def pixel_match():
    expected_color = (60, 45, 48)

    x, y = 2127, 374

    if pyautogui.pixelMatchesColor(x, y, expected_color):
        print("Цвет пикселя совпадает с ожидаемым!!")
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
        expected_color = (242, 180, 162)
        time.sleep(0.3)
        if pyautogui.pixelMatchesColor(1940, 446, expected_color):
            pyautogui.click(1940, 446)
        else:
            print("no")
    else:
        print("Цвет пикселя не совпадает с ожидаемым.(")


if __name__ == "__main__":
    pixel_match()
