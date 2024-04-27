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


def move_cursor_to_specified_window(title):
    try:
        # Ищем окно по его заголовку
        window = gw.getWindowsWithTitle(title)
        if window:
            window = window[0]  # Берем первое окно, если найдено несколько
            if window.isMinimized:
                window.restore()  # Восстанавливаем окно, если оно свернуто

            # Получаем координаты окна
            center_x = window.left  # + (window.width // 2)
            center_y = window.top  # + (window.height // 2)

            # Перемещаем курсор к центру найденного окна
            pyautogui.moveTo(center_x, center_y)
            print(f"Курсор успешно перемещен в центр окна '{title}' на координаты ({center_x}, {center_y}).")
        else:
            print(f"Окно с заголовком '{title}' не найдено.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    move_cursor_to_specified_window("(1) ChatGPT4 | Midjourney – (1)")
