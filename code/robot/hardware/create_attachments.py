from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor


def create_attachments():
    left_attachment = Motor(
        port=Port.B,
        positive_direction=Direction.CLOCKWISE,
        reset_angle=True,
    )
    right_attachment = Motor(
        port=Port.F,
        positive_direction=Direction.CLOCKWISE,
        reset_angle=True,
    )
    return left_attachment, right_attachment
