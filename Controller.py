import hid
import time

# List all devices
# for device in hid.enumerate():
#     print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x1209, 0x4f54)
gamepad.set_nonblocking(True)

while True:
    report = gamepad.read(64)
    if report:
        controller = {
            "Aileron: ": [report[3], report[4]],
            "Elevator: ": [report[5], report[6]],
            "Throttle: ": [report[7], report[8]],
            "Rudder: ": [report[9], report[10]],
            "Toggle: ": [report[13], report[15]],
            "Momentary: ": [report[11], report[12]]
        }
        print(controller)

    # time.sleep(1)

# https://blog.thea.codes/talking-to-gamepads-without-pygame/