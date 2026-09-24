from pybricks.parameters import Button
from pybricks.tools import wait


def wait_for_left_button(hub):
    while Button.LEFT not in hub.buttons.pressed():
        wait(10)
