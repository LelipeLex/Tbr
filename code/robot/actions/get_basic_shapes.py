from .wait_for_left_button import wait_for_left_button


def get_basic_shapes(get_blue, get_red, get_green, hub):
    get_blue()
    wait_for_left_button(hub)
    get_red()
    wait_for_left_button(hub)
    get_green()
