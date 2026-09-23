from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

def RunTeste():
    if hub.imu.ready():
        print(hub.imu.heading())
        from main import setMotors, Turn
        setMotors()
        Turn(90)
        print(hub.imu.heading())