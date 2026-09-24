from pybricks.tools import wait

from ..hardware.create_drive_base import create_drive_base
from ..hardware.create_hub import create_hub
from ..movement.turn import turn


def run_test():
    hub = create_hub()
    motors = create_drive_base()

    while not hub.imu.ready():
        print("IMU not ready")
        wait(1000)

    print(hub.imu.heading())
    turn(hub, motors, 90)
    print(hub.imu.heading())
