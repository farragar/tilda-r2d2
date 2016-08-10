from http_client import get
import pyb
from imu import IMU
import wifi

TILT_THRESHOLD = -0.4
TILT_PLAY = -0.1

imu = IMU()
host = 'http://192.168.0.12:8001'

if not wifi.nic().is_connected():
    wifi.connect(timeout=20)

triggered = False

while(True):
    _, y, _ = imu.get_acceleration()

    if(y < TILT_THRESHOLD):
	triggered = True
    elif(y > TILT_PLAY and triggered): 
        try:
            get(host, timeout=10, is_ip=True).raise_for_status()
        except Exception as e:
            print('Request Failed {}'.format(str(e)))
        except OSError as e:
            print('Request Failed {}'.format(str(e)))
        finally:
            triggered = False

    pyb.delay(500)
