import pyautogui


def get_current_color_and_position():
    current_position = pyautogui.position()
    x, y = current_position
    print(f'x = {x}, y = {y}')
    # функция pixel возвращает по x и y код цвета
    current_color = pyautogui.pixel(x, y)
    print(current_color)

    return x, y, current_color


if __name__ == "__main__":
    get_current_color_and_position()
