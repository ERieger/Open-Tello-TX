from djitellopy import Tello
drone = Tello()

drone.connect()

drone.takeoff()
drone.move_forward(100)
drone.rotate_clockwise(180)
drone.move_forward(100)
drone.land()
