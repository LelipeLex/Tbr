from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Direction, Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait


print("Iniciando programa")
hub = PrimeHub()
program = 1

sensor = ColorSensor(Port.C)


def set_motors():
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E, Direction.CLOCKWISE)
    motors = DriveBase(left_motor, right_motor, 55.8, 87)
    motors.settings(straight_speed=900, straight_acceleration=900)
    return motors


def normalize_angle(angle):
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle


def turn(degrees):
    target = normalize_angle(hub.imu.heading() + degrees)
    integral = 0
    previous_error = 0

    while True:
        current_heading = hub.imu.heading()
        error = normalize_angle(target - current_heading)
        integral += error
        derivative = error - previous_error
        previous_error = error

        if abs(error) < 0.9:
            motors.stop()
            break

        kp = 3.2
        ki = 0.02
        kd = 0.8

        turn_rate = (kp * error) + (ki * integral) + (kd * derivative)
        speed = max(-180, min(180, turn_rate))

        if abs(speed) < 18 and abs(error) > 0:
            speed = 18 if error > 0 else -18

        motors.drive(0, int(speed))
        wait(12)

    motors.stop()


def penalty1():
    motors.straight(200)
    right_attachment.run_time(1000, 3500)
    motors.straight(-200)
    right_attachment.run_time(-1000, 3500)


def get_blue():
    motors.straight(60)
    turn(90)
    motors.straight(22.5)
    right_attachment.run_time(1000, 3500)
    turn(-90)
    motors.straight(570)
    turn(90)
    motors.straight(53)
    right_attachment.run_time(-1000, 2500)
    motors.straight(-47)
    turn(90)
    motors.straight(570)


def get_green():
    motors.straight(165)
    turn(90)
    motors.straight(180)
    right_attachment.run_time(1000, 4000)
    motors.straight(-160)
    turn(-90)
    motors.straight(405)
    turn(90)
    motors.straight(30)
    right_attachment.run_time(-1000, 2500)
    motors.straight(-30)
    turn(-84)
    motors.straight(-500)


def get_red():
    motors.straight(250)
    turn(90)
    motors.straight(115)
    right_attachment.run_time(1000, 2500)
    motors.straight(175)
    turn(-90)
    motors.straight(25)
    right_attachment.run_time(-1000, 2500)
    motors.straight(-25)
    turn(90)
    motors.straight(-279)


def put_blue():
    motors.straight(650)
    turn(180)
    motors.straight(700)


def put_green():
    motors.straight(435)
    motors.turn(74)
    motors.straight(50)
    motors.straight(85)
    turn(0)
    motors.straight(30)


def get_high_red():
    motors.straight(290)
    turn(-90)
    motors.straight(160)
    turn(90)
    motors.straight(30)
    right_attachment.run_time(1000, 2500)
    motors.straight(-70)
    turn(-90)
    motors.straight(40)
    right_attachment.run_time(-1000, 2500)


def get_high_blue():
    motors.straight(290)
    turn(-90)
    motors.straight(310)
    turn(90)
    motors.straight(520)
    turn(-90)
    motors.straight(43)
    right_attachment.run_time(1000, 2500)
    motors.straight(-80)
    turn(90)
    motors.straight(-385)
    turn(-90)
    motors.straight(-400)
    right_attachment.run_time(-1000, 2500)


def car():
    motors.straight(840)
    motors.straight(-840)


def clean():
    motors.straight(200000)


def choose_program():
    global program

    programs = [
        get_blue,
        get_green,
        get_red,
        car,
        get_high_red,
        get_high_blue,
        penalty1,
        clean,
    ]

    hub.display.number(program)
    pressed = hub.buttons.pressed()

    if sensor.color() == Color.BLUE:
        programs[program - 1]()
    elif Button.LEFT in pressed and Button.RIGHT not in pressed:
        wait(250)
        if Button.LEFT in hub.buttons.pressed():
            program -= 1
    elif Button.RIGHT in pressed and Button.LEFT not in pressed:
        wait(250)
        if Button.RIGHT in hub.buttons.pressed():
            program += 1

    program = max(1, min(program, len(programs)))


motors = set_motors()
left_attachment = Motor(Port.B, Direction.CLOCKWISE, reset_angle=True)
right_attachment = Motor(Port.F, Direction.CLOCKWISE, reset_angle=True)
print("Hardware pronto")

while True:
    choose_program()
    wait(10)