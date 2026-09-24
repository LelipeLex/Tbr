from pybricks.parameters import Button
from pybricks.tools import wait


def get_program(hub, program, programs):
    hub.display.number(program)
    pressed = hub.buttons.pressed()

    if Button.LEFT in pressed and Button.RIGHT in pressed:
        programs[program - 1]()
    elif Button.LEFT in pressed and Button.RIGHT not in pressed:
        wait(250)
        if Button.LEFT in hub.buttons.pressed():
            program -= 1
    elif Button.RIGHT in pressed and Button.LEFT not in pressed:
        wait(250)
        if Button.RIGHT in hub.buttons.pressed():
            program += 1

    return max(1, min(program, len(programs)))
