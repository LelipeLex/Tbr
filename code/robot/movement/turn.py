def turn(hub, motors, degrees_to_turn):
    initial = hub.imu.heading()
    target = initial + degrees_to_turn
    target += 1 if degrees_to_turn > 0 else -1

    while True:
        error = target - hub.imu.heading()
        if abs(error) < 1:
            break

        speed = max(-300, min(300, error * 12))
        if 0 < speed < 80:
            speed = 80
        elif -80 < speed < 0:
            speed = -80

        motors.drive(0, speed)

    motors.stop()
