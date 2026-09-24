from pybricks.parameters import Button
from pybricks.tools import wait


def penalty1(motors, right_attachment):
    motors.straight(200)
    right_attachment.run_time(1000, 3500)
    motors.straight(-200)
    right_attachment.run_time(-1000, 3500)


def get_blue(motors, right_attachment, turn):
    motors.straight(60)
    turn(86)
    motors.straight(123)
    right_attachment.run_time(1000, 3500)
    turn(-86)
    motors.straight(570)
    turn(88)
    motors.straight(53)
    right_attachment.run_time(-1000, 2500)
    motors.straight(-47)
    turn(90)
    motors.straight(570)


def get_green(motors, right_attachment, turn):
    motors.straight(165)
    turn(84)
    motors.straight(220)
    right_attachment.run_time(1000, 4000)
    motors.straight(-160)
    turn(-71)
    motors.straight(405)
    turn(80)
    motors.straight(30)
    right_attachment.run_time(-1000, 2500)
    motors.straight(-30)
    turn(-90)
    motors.straight(-500)


def get_red(motors, right_attachment, turn):
    motors.straight(250)
    turn(82)
    motors.straight(115)
    right_attachment.run_time(1000, 2500)
    motors.straight(175)
    turn(-90)
    motors.straight(25)
    right_attachment.run_time(-1000, 2500)
    motors.straight(-25)
    turn(70)
    motors.straight(-279)


def put_blue(motors, turn):
    motors.straight(650)
    turn(180)
    motors.straight(700)


def put_green(motors, turn):
    motors.straight(435)
    motors.turn(74)
    motors.straight(50)
    motors.straight(85)
    turn(2)
    motors.straight(30)


def get_high_red(motors, right_attachment, turn):
    motors.straight(290)
    turn(-90)
    motors.straight(160)
    turn(90)
    motors.straight(30)
    right_attachment.run_time(1000, 2500)
    motors.straight(-70)
    turn(-45)
    motors.straight(40)
    right_attachment.run_time(-1000, 2500)


def get_high_blue(motors, right_attachment, turn):
    motors.straight(290)
    turn(-90)
    motors.straight(310)
    turn(90)
    motors.straight(520)
    turn(-105)
    motors.straight(43)
    right_attachment.run_time(1000, 2500)
    motors.straight(-80)
    turn(105)
    motors.straight(-385)
    turn(-45)
    motors.straight(-400)
    right_attachment.run_time(-1000, 2500)


def car(motors):
    motors.straight(840)
    motors.straight(-840)


def clean(motors):
    motors.straight(200000)


def get_basic_shapes(get_blue_action, get_red_action, get_green_action, hub):
    get_blue_action()
    _wait_for_left_button(hub)
    get_red_action()
    _wait_for_left_button(hub)
    get_green_action()


def _wait_for_left_button(hub):
    while Button.LEFT not in hub.buttons.pressed():
        wait(10)
