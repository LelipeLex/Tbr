from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase


def create_drive_base():
    left_motor = Motor(
        port=Port.A,
        positive_direction=Direction.COUNTERCLOCKWISE,
    )
    right_motor = Motor(
        port=Port.E,
        positive_direction=Direction.CLOCKWISE,
    )
    motors = DriveBase(left_motor, right_motor, 55.8, 87)
    motors.settings(straight_speed=900, straight_acceleration=900)
    return motors
