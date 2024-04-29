import pyautogui
from nebuSphere import auxiliary
from time import sleep


def exp_sphere_pixel_cycle():
    win_x, win_y = auxiliary.get_win_coords("Карась")
    region = (win_x, win_y, 1430, 810)
    target_color = (86, 138, 206)

    screenshot = pyautogui.screenshot(region=region)
    while True:
        for x in range(region[2]):
            for y in range(region[3]):
                pixel_color = screenshot.getpixel((x, y))

                if pixel_color == target_color:
                    pyautogui.click(win_x + x, win_y + y)
                    pyautogui.mouseDown()
                    pyautogui.press("w")
                    sleep(1.5)
                    pyautogui.mouseUp()
                    screenshot = pyautogui.screenshot(region=region)
