from . import experimental
from nebuSphere import auxiliary


def get_distance():
    # TODO: Вычислять насколько относительно игрока смещать курсор (Игрок == найденный красный цвет)
    # Использовать это расстояние для того, чтобы определить сколько потребуется времени игроку,
    # чтобы добраться до объекта
    pass


def get_direction_angle():
    win_x, win_y = auxiliary.get_win_coords("Карась")
    x, y = auxiliary.search_color_in_game("Карась", (86, 138, 206))
    # TODO: вычислять угол и применять его к джойстику на другом окне

