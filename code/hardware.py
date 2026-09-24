from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase


def create_hardware():
    hub = PrimeHub()
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.E, Direction.CLOCKWISE)
    motors = DriveBase(left_motor, right_motor, 55.8, 87)
    motors.settings(straight_speed=900, straight_acceleration=900)
    left_attachment = Motor(Port.B, Direction.CLOCKWISE, reset_angle=True)
    right_attachment = Motor(Port.F, Direction.CLOCKWISE, reset_angle=True)
    return hub, motors, left_attachment, right_attachment
