from . import auxiliary
from . import data
from . import nebu
from . import sphere


def start():
    auxiliary.get_current_color_and_position()


def dash():
    sphere.experimental.exp_sphere_pixel_cycle("Карась")
