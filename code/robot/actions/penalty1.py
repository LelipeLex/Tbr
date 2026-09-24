def penalty1(motors, right_attachment):
    motors.straight(200)
    right_attachment.run_time(1000, 3500)
    motors.straight(-200)
    right_attachment.run_time(-1000, 3500)
