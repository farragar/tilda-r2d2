### author: Laurie James
### description: updates and installs apps. To publish apps use https://badge.emfcamp.org
### license: MIT
### reboot-before-run: True
### Appname: R2D2 bin player

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
    y = imu.get_acceleration()['y']

    if(int(y) < TILT_THRESHOLD):
	triggered = True
    elif(y > TILT_PLAY and triggered): 
        try:
            print('foobar')
            get(host, timeout=10).raise_for_status()
        except Exception as e:
            print('Request Failed {}'.format(str(e)))
        except OSError as e:
            print('Request Failed {}'.format(str(e)))
        finally:
            triggered = False

    pyb.delay(500)
