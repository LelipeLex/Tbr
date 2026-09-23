from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

program = 1


def setMotors():

    left_motor = Motor(
        port=Port.A,
        positive_direction=Direction.COUNTERCLOCKWISE
    )

    right_motor = Motor(
        port=Port.E,
        positive_direction=Direction.CLOCKWISE
    )

    motors = DriveBase(left_motor, right_motor, 55.8, 87)

    motors.settings(
        straight_speed=900,
        straight_acceleration=900,
    )

    return motors


def Turn(degrees_to_turn):

    initial = hub.imu.heading()
    target = initial + degrees_to_turn

    if degrees_to_turn > 0:
        target += 1
    else:
        target -= 1

    while True:

        error = target - hub.imu.heading()

        if abs(error) < 1:
            break

        speed = error * 12

        if speed > 300:
            speed = 300

        if speed < -300:
            speed = -300

        if 0 < speed < 80:
            speed = 80

        if -80 < speed < 0:
            speed = -80

        motors.drive(0, speed)

    motors.stop()


left_attachment = Motor(
    port=Port.B,
    positive_direction=Direction.CLOCKWISE,
    reset_angle=True
)

right_attachment = Motor(
    port=Port.F,
    positive_direction=Direction.CLOCKWISE,
    reset_angle=True
)


# penaltys

def penalty1():

    motors.straight(200)

    right_attachment.run_time(1000, 3500)

    motors.straight(-200)

    right_attachment.run_time(-1000, 3500)


# get shapes

def get_blue():

    motors.straight(60)

    Turn(86)

    motors.straight(123)

    right_attachment.run_time(1000, 3500)

    Turn(-86)

    motors.straight(570)
    
    Turn(88)

    motors.straight(53)

    right_attachment.run_time(-1000, 2500)

    motors.straight(-47)
    
    Turn(90)

    motors.straight(570)


def get_green():

    motors.straight(165)

    Turn(84)

    motors.straight(220)

    right_attachment.run_time(1000, 4000)

    motors.straight(-160)

    Turn(-71)

    motors.straight(405)

    Turn(80)

    motors.straight(30)

    right_attachment.run_time(-1000, 2500)

    motors.straight(-30)

    Turn(-90)

    motors.straight(-500)


def put_green():
    motors.straight(435)
    motors.turn(74)
    motors.straight(50)
    motors.straight(85)
    Turn(2)
    motors.straight(30)

def get_red():
    motors.straight(250)

    Turn(82)

    motors.straight(115)

    right_attachment.run_time(1000, 2500)

    motors.straight(175)

    Turn(-90)

    motors.straight(25)

    right_attachment.run_time(-1000, 2500)

    motors.straight(-25)
    Turn(70)
    motors.straight(-279)

def put_blue():
    motors.straight(650)
    Turn(180)
    motors.straight(700)


def get_basic_shapes():

    get_blue()

    while True:

        if Button.LEFT in hub.buttons.pressed():
            break

        wait(10)

    get_red()

    while True:

        if Button.LEFT in hub.buttons.pressed():
            break

        wait(10)

    get_green()


def car():

    motors.straight(840)

    motors.straight(-840)


# get high shapes

def get_high_red():

    motors.straight(290)

    Turn(-90)

    motors.straight(160)

    Turn(90)

    motors.straight(30)

    right_attachment.run_time(1000, 2500)

    motors.straight(-70)

    Turn(-45)

    motors.straight(40)

    right_attachment.run_time(-1000, 2500)


def get_high_blue():

    motors.straight(290)

    Turn(-90)

    motors.straight(310)

    Turn(90)

    motors.straight(520)

    Turn(-105)

    motors.straight(43)

    right_attachment.run_time(1000, 2500)

    motors.straight(-80)

    Turn(105)

    motors.straight(-385)

    Turn(-45)

    motors.straight(-400)

    right_attachment.run_time(-1000, 2500)


def clean():

    motors.straight(200000)


def get_program():

    global program

    hub.display.number(program)

    pressed = hub.buttons.pressed()

    programs = [
        get_blue,
        get_green,
        get_red,
        car,
        get_high_red,
        get_high_blue,
        penalty1,
        clean
    ]

    if Button.LEFT in pressed and Button.RIGHT in pressed:

        programs[program - 1]()

    elif Button.LEFT in pressed and Button.RIGHT not in pressed:

        wait(250)

        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed and Button.RIGHT not in pressed:
            program -= 1

    elif Button.RIGHT in pressed and Button.LEFT not in pressed:

        wait(250)

        pressed = hub.buttons.pressed()

        if Button.RIGHT in pressed and Button.LEFT not in pressed:
            program += 1

    if program <= 0:
        program = 1

    elif program > len(programs):
        program = len(programs)


motors = setMotors()

from teste import RunTeste
RunTeste()

#if hub.imu.ready():
#    while True:
#        get_program()
#        wait(10)