import pyautogui
import x_y_now_funcs


def pixel_match():
    expected_color = (150, 110, 103)

    x, y = 2128, 366

    if pyautogui.pixelMatchesColor(x, y, expected_color):
        print("Цвет пикселя совпадает с ожидаемым!!")
    else:
        print("Цвет пикселя не совпадает с ожидаемым.(")


if __name__ == "__main__":
    pixel_match()
