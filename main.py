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
TILT_PLAY = -0.1

host = 'http://192.168.0.10'

if not wifi.nic().is_connected():
    wifi.connect(timeout=20)

triggered = False

while(True):
    y = imu.get_acceleration()['y']
    ugfx.clear()

    ugfx.text(5, 5, str(y), ugfx.RED)

    if(y < TILT_THRESHOLD):
	triggered = True
    elif(y > TILT_PLAY and triggered): 
        try:
            get(host, timeout=10).raise_for_status()
        except Exception as e:
            print('Request Failed {}'.format(str(e)))
        except OSError as e:
            print('Request Failed {}'.format(str(e)))
        finally:
            triggered = False
