import pyautogui
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


def move_cursor_to_specified_window(title):
    print("Выполнение функции: move_cursor_to_specified_window\n")
    try:
        # Ищем окно по его заголовку
        window = gw.getWindowsWithTitle(title)
        if window:
            window = window[0]  # Берем первое окно, если найдено несколько
            if window.isMinimized:
                window.restore()  # Восстанавливаем окно, если оно свернуто

            # Получаем координаты окна
            x_win = window.left
            y_win = window.top

            # Перемещаем курсор к найденному окна
            pyautogui.moveTo(x_win, y_win)
            print(f"Курсор успешно перемещен в краю окна '{title}' на координаты ({x_win}, {y_win}).")
            return x_win, y_win
        else:
            print(f"Окно с заголовком '{title}' не найдено.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
