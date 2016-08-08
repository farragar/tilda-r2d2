import ugfx
import buttons
import pyb
from http_client import get
from imu import IMU

ugfx.init()
ugfx.text(5, 5, 'Hello world!', ugfx.RED)
imu = IMU()
TILT_THRESHOLD = -0.4

host = 'http://www.farragar.com'
port = 80


while(True):
    y = imu.get_acceleration()['y']
    ugfx.clear()

    ugfx.text(5, 5, str(y), ugfx.RED)

    if(y > TILT_THRESHOLD):
    	get('{}:{}'.format(host, port))