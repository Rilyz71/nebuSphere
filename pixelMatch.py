import pyautogui
from x_y_now_funcs import current_position

"""
Имеет ли пиксель на позиции (100, 200)
 на экране цвет (130, 135, 144). 
"""

expected_color = (255, 255, 255)

x, y = current_position

if pyautogui.pixelMatchesColor(x, y, expected_color):
    print("Цвет пикселя совпадает с ожидаемым!")
else:
    print("Цвет пикселя не совпадает с ожидаемым.")