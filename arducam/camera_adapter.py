import RPi.GPIO as gp
import os

CAM_ROOT = 0
CAM_SIDE = 1
CAM_AERIAL = 2
CAM_DISCONNECTED = 3

class CameraAdapter:
    def __init__(self):
        gp.setmode(gp.BOARD)
        gp.setup(7, gp.OUT)
        gp.setup(11, gp.OUT)
        gp.setup(12, gp.OUT)
    
    def change_camera(self, cam):
        if cam == CAM_ROOT:
            i2c_addr = 0x04
            pin7 = False
            pin11 = False
            pin12 = True
        elif cam == CAM_SIDE:
            i2c_addr = 0x05
            pin7 = True
            pin11 = False
            pin12 = True
        elif cam == CAM_AERIAL:
            i2c_addr = 0x06
            pin7 = False
            pin11 = True
            pin12 = False
        elif cam == CAM_DISCONNECTED:
            i2c_addr = 0x07
            pin7 = True
            pin11 = True
            pin12 = False
        else:
            raise ValueError(f'unknown camera {cam}')
        i2c_set_cmd = f'i2cset -y 1 0x70 0x00 {i2c_addr}'
        os.system(i2c_set_cmd)
        gp.output(7, pin7)
        gp.output(11, pin11)
    
    
    def capture(self, filepath = 'capture.jpg'):
        if os.path.exists(filepath):
            os.remove(filepath)
        cmd = f'libcamera-still -o {filepath}'
        os.system(cmd)
