from inputs import get_gamepad
from inputs import devices
from djitellopy import tello

for device in devices:
    print(device)


takeoff = False

drone = tello.Tello()
drone.connect()

while takeoff == False:
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)

        if (event.code == 'ABS_RZ'):
            if (event.state == 2047):
                drone.takeoff()
                takeoff = True

def scale(x):
    return int((x / 2047) * 200) - 100

while takeoff:
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)

        if (event.code == 'ABS_RY'):
            if (event.state == 2047):
                drone.emergency()
        if (event.code == 'ABS_RZ'):
            if (event.state == 0):
                drone.land()
                takeoff = False
        if(event.code == 'ABS_X'):
            drone.send_rc_control(scale(event.state), 0, 0, 0)
        if(event.code == 'ABS_Y'):
            drone.send_rc_control(0, scale(event.state), 0, 0)
        if(event.code == 'ABS_THROTTLE'):
            drone.send_rc_control(0, 0, scale(event.state), 0)
        if(event.code == 'ABS_RX'):
            drone.send_rc_control(0, 0, 0, scale(event.state))


