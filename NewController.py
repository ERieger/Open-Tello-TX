import hid
from djitellopy import tello

# List all devices
for device in hid.enumerate():
    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

drone = tello.Tello()
drone.connect()

flyState = False

while flyState == False:
    
