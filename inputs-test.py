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

def send_rc(command):
    drone.send_rc_control(command.a, command.e, command.t, command.r)

while takeoff:
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)

        command = {
            "ail": 0,
            "ele": 0,
            "thr": 0,
            "rud": 0
        }

        if (event.code == 'ABS_RY'):
            if (event.state == 2047):
                drone.emergency()
        if (event.code == 'ABS_RZ'):
            if (event.state == 0):
                drone.land()
                takeoff = False
        if(event.code == 'ABS_X'):
            command.a = scale(event.state)
        if(event.code == 'ABS_Y'):
            command.e = scale(event.state)
        if(event.code == 'ABS_THROTTLE'):
            command.t = scale(event.state)
        if(event.code == 'ABS_RX'):
            command.r = scale(event.state)
        
        send_rc(command)
