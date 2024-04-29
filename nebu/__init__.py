from coefficients import *
from auxiliary import *
import pyautogui
from time import sleep
import pytesseract
from PIL import Image


def after_death_tap_start(win_title):
    """
    Нажимает "Играть" сразу же после смерти игрока
    Для безопасности после клика ожидание = 2 секунды
    :return:
    """
    win_x, win_y = get_win_coords(win_title)

    x = win_x + X_COEFF_1280_PLAYBUTTON
    y = win_y + Y_COEFF_1280_PLAYBUTTON

    expected_color = (154, 7, 87)

    while True:
        if pyautogui.pixelMatchesColor(x, y, expected_color):
            pyautogui.click(x, y)
            sleep(2)


def antioffline(win_title: str):
    target_color = (115, 175, 170)

    # + Отслеживание положения окна каждый 1.5 сек
    while True:
        win_x, win_y = get_win_coords(win_title)
        x = win_x + X_COEFF_1280_ANTIOFF_SIGH
        y = win_y + Y_COEFF_1280_ANTIOFF_SIGH
        pixel = pyautogui.pixelMatchesColor(x, y, target_color)

        print(f"Checked - {x}, {y}")

        if pixel:
            pyautogui.click(x, y)
        sleep(1.5)


def get_score_from_screen(win_title: str):
    """
    Только для трёхзначных и более чисел.
    Функция сканирует область экрана, где находится счёт игрока.
    :param win_title: Название окна
    :return: Счёт игрока
    """

    # ФУНКЦИЯ НЕ ВИДИТ ДВУЗНАЧНЫЕ ЧИСЛА

    win_x, win_y = get_win_coords(win_title)
    x = win_x + X_COEFF_1280_SCORE
    y = win_y + Y_COEFF_1280_SCORE
    screenshot = pyautogui.screenshot(region=(x, y, WIDTH_COEFF_1280_SCORE,
                                              HEIGHT_COEFF_1280_SCORE))

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    screenshot.save('score.png')
    image = Image.open('score.png')
    score = pytesseract.image_to_string(image)
    print(f"Score: {score.strip()}")
    return score.strip()


def text_in_chat(msg: str, win_title: str = "No Name"):
    winx, winy = get_win_coords(win_title)
    pyautogui.click(winx + X_COEFF_1280_CHAT_LINE, winy + Y_COEFF_1280_CHAT_LINE)
    pyautogui.write(msg)

    x = winx + X_COEFF_1280_ENTER_CHAT
    y = winy + Y_COEFF_1280_ENTER_CHAT

    pyautogui.click(x, y)


def score_chat_cycle(n: int, score_from_win: str = "Карась"):
    for i in range(1, n):
        score = get_score_from_screen(score_from_win)
        text_in_chat(f"Score: {score}")
        sleep(1.9)
