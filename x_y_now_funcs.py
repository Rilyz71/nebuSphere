import pyautogui

current_position = pyautogui.position()

x, y = current_position
print(f'x = {x}, y = {y}')

# функция pixel возвращает по x и y код цвета
current_color = pyautogui.pixel(x, y)
print(current_color)
