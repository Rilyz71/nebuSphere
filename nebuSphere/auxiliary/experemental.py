import pyautogui
import pygetwindow as gw


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
