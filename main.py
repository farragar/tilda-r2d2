import ugfx
import buttons
import pyb
from http_client import get
from imu import IMU
import wifi

ugfx.init()
ugfx.text(5, 5, 'Hello world!', ugfx.RED)
imu = IMU()
TILT_THRESHOLD = -0.4

host = 'http://192.168.0.10'

if not wifi.nic().is_connected():
    wifi.connect(timeout=20)

waiting = False

while(True):
    if waiting > 0:
        waiting -= 1

    y = imu.get_acceleration()['y']
    ugfx.clear()

    ugfx.text(5, 5, str(y), ugfx.RED)

    if(y < TILT_THRESHOLD and not waiting):
        try:
            print('Issuing query')
            awaiting_response = get(host).raise_for_status()
            waiting = 10000
        except Exception as e:
            print('Query Failed {}'.format(str(e)))
        except OSError as e:
            print('Query Failed {}'.format(str(e)))
    elif waiting:
        print(waiting)
