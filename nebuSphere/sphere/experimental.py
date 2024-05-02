import pyautogui
from nebuSphere import auxiliary
from time import sleep


def exp_sphere_pixel_cycle(win_title: str):
    win_x, win_y = auxiliary.get_win_coords(win_title)
    region = (win_x, win_y, 1430, 810)
    sphere_color = (86, 138, 206)

    rainbow_sphere_color = (203, 110, 132)
    rsc2 = (252, 209, 202)

    # TODO: 1 Сделать библиотеку цветов сфер (штук 10-15 для обычной и разноцветной)

    while True:
        screenshot = pyautogui.screenshot(region=region)
        for x in range(region[2]):
            for y in range(region[3]):
                pixel_color = screenshot.getpixel((x, y))

                if pixel_color == sphere_color:
                    return x, y
        sleep(5)
