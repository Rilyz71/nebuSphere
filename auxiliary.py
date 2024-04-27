import pygetwindow as gw
import pyautogui


# ФАЙЛ ДЛЯ ВСПОМОГАТЕЛЬНЫХ ФУНКЦИЙ, КОТОРЫЕ РАБОТАЮТ С КООРДИНАТАМИ, ОКНАМИ И ПРОЧИМИ ВЕЩАМИ

def get_win_coords(win_title: str):
    try:
        # В АРГУМЕНТЫ ВВЕСТИ КООРДИНАТЫ ТРЕБУМОЙ ЗОНЫ (В КОТОРУЮ ПЕРЕДВИГАТЬ КУРСОР)
        window = gw.getWindowsWithTitle(win_title)
        if window:
            window = window[0]  # Берем первое окно, если найдено несколько
            if window.isMinimized:
                window.restore()  # Восстанавливаем окно, если оно свернуто

            # Получаем координаты окна
            x_win = window.left
            y_win = window.top
            return x_win, y_win
        else:
            print("Окно с данным названием не найдено")
    except Exception as e:
        print(f"Произошла ошибка {e}")


def calculate_koeffs(win_title: str, x_input, y_input):
    """
    Функция возвращает коэффициенты на которые нужно суммировать координаты левого верхнего края
    окна, чтобы получить требуемые координаты, что пользователь передал в аргументы.
    :param win_title: Название окна с которым функция будет работать.
    :param x_input: Требуемый икс.
    :param y_input: Требуемый игрек.
    :return: Коэффициенты, на которые нужно суммировать координаты левого верхнего края окна,
     чтобы получить значения передаваемых координат X и Y.
    """

    x_win, y_win = get_win_coords(win_title)
    koeffs = x_input - x_win, y_input - y_win
    return koeffs


def get_all_windows():
    """
    Выводит список названий всех открытых окон
    :return: all_windows
    """
    all_windows = gw.getAllWindows()

    for window in all_windows:
        print(window.title)
    return all_windows


def get_current_color_and_position():
    current_position = pyautogui.position()
    x, y = current_position
    print(f'x = {x}, y = {y}')
    # функция pixel возвращает по x и y код цвета
    current_color = pyautogui.pixel(x, y)
    print(current_color)

    return x, y, current_color
