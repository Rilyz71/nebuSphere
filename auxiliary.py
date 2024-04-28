import pygetwindow as gw
import pyautogui


# ФАЙЛ ДЛЯ ВСПОМОГАТЕЛЬНЫХ ФУНКЦИЙ

def get_win_coords(win_title: str):
    try:
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


def count_pixel_with_target_color(region=(1017, 444, 90, 630), target_color=(254, 0, 161),
                                  autoprint=0, matrix=0):
    """
    Вывод данных:
                    for coords in found_pixels:
                    print(coords)

    Функция подсчитывает и выводит количество пикселей с заданным цветом в определённой области
    :param region: x, y, ширина, высота
    :param target_color: цвет
    :param autoprint: Автовывод данных принтом
    :param matrix: Вывод матрицы с координатами пикселей (а не количество)
    :return:
    """
    # x, y, ширина (по x), высота (по y)
    screenshot = pyautogui.screenshot(region=region)

    count = 0
    found_pixels = []
    for x in range(region[2]):
        for y in range(region[3]):
            pixel_color = screenshot.getpixel((x, y))

            if pixel_color == target_color:
                count += 1
                abs_x = x + region[0]
                abs_y = y + region[1]

                if matrix == 1:
                    found_pixels.append((abs_x, abs_y))

                if autoprint == 1:
                    print(f"{count} Пиксель найден на позиции {abs_x}, {abs_y}")

    if count == 0:
        print("Пиксели не найдены.")

    return found_pixels if matrix == 1 else count


if __name__ == "__main__":
    get_current_color_and_position()
