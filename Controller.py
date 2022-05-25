import hid
import time
from djitellopy import tello

# List all devices
# for device in hid.enumerate():
#    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

drone = tello.Tello()
drone.connect()

gamepad = hid.device
gamepad.open(0x1209,0x4f54)
gamepad.set_nonblocking(True)

takeoff = False

def getReport():
    global controller
    report = gamepad.read(64)
    if report:
        controller = {
            "Aileron": report[3] | report[4] << 8,
            "Elevator": report[5] | report[6] << 8,
            "Throttle": report[7] | report[8] << 8,
            "Rudder": report[9] | report[10] << 8,
            "Toggle": report[13],
            "Momentary": [report[11], report[12]]
        }
        print(controller)

    return controller

while takeoff == False:
    controller = getReport()
    print(controller["Toggle"])
    if (controller["Toggle"] == 255):
        drone.takeoff()
        takeoff = True

def scale(x):
    return int((x / 2047) * 200) - 100

while takeoff:
    controller = getReport()
    if (controller["Toggle"] == 0):
        drone.takeoff()
        takeoff = False

    drone.send_rc_control(scale(controller["Aileron"]), scale(controller["Elevator"]), scale(controller["Throttle"]), scale(controller["Rudder"]))
    time.sleep(0.1)

# 11-bit aileron, rudder, elevator, throttle control
# report[3] | report[4] << 8
# https://blog.thea.codes/talking-to-gamepads-without-pygame/
