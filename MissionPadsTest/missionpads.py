from djitellopy import Tello

tello = Tello()
tello.connect()

tello.enable_mission_pads()

tello.takeoff()

pad = tello.get_mission_pad_id()

while pad != 1:
    if pad == 5:
        tello.send_rc_control(0, 20, 0, 30)

    pad = tello.get_mission_pad_id()

tello.send_rc_control(0, 0, 0, 0)
tello.disable_mission_pads()
tello.land()
tello.end()