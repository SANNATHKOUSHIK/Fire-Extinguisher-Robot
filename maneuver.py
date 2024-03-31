import Jetson.GPIO as GPIO
import time

class Manuever:
    def __init__(self,fl_1:int,fl_2:int,fr_1:int,fr_2:int,bl_1:int,bl_2:int,br_1:int,br_2:int,fr_e:int,fl_e:int,bl_e:int,br_e:int,pump:int,servo:int,ir:int):
        self.fl_1 = fl_1
        self.fl_2 = fl_2
        self.fr_1 = fr_1
        self.fr_2 = fr_2
        self.bl_1 = bl_1
        self.bl_2 = bl_2
        self.br_1 = br_1
        self.br_2 = br_2
        self.fr_e = fr_e
        self.fl_e = fl_e
        self.bl_e = bl_e
        self.br_e = br_e
        self.ir = ir
        self.p = pump
        self.servo = servo
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(fr_e , GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(fl_e , GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(br_e , GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(bl_e , GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(fr_1 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(fr_2 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(fl_1 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(fl_2 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(bl_1 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(bl_2 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(br_1 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(br_2 , GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(servo, GPIO.OUT)
        GPIO.setup(ir,GPIO.IN)
        self.pwm = GPIO.PWM(self.servo,50)
        self.pwm.start(4.95)
        self.angle =90

    def forward(self):
        GPIO.output(self.fl_1 , GPIO.HIGH)
        GPIO.output(self.fl_2 , GPIO.LOW)
        GPIO.output(self.fr_1 , GPIO.HIGH)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.HIGH)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.HIGH)
        GPIO.output(self.br_1 , GPIO.LOW)

    def backward(self):
        GPIO.output(self.fl_2 , GPIO.HIGH)
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.HIGH)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.HIGH)
        GPIO.output(self.bl_1 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.HIGH)
        GPIO.output(self.br_2 , GPIO.LOW)

    def slide_right(self):
        GPIO.output(self.fl_2 , GPIO.LOW)
        GPIO.output(self.fl_1 , GPIO.HIGH)
        GPIO.output(self.fr_2 , GPIO.HIGH)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.HIGH)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.HIGH)

    def slide_left(self):
        GPIO.output(self.fl_2 , GPIO.HIGH)
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.fr_1 , GPIO.HIGH)
        GPIO.output(self.bl_1 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.HIGH)
        GPIO.output(self.br_2 , GPIO.HIGH)
        GPIO.output(self.br_1 , GPIO.LOW)

    def clockwise_rotation(self):
        GPIO.output(self.fl_2 , GPIO.HIGH)
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fr_1 , GPIO.HIGH)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.HIGH)
        GPIO.output(self.br_2 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.HIGH)

    def anticlockwise_rotation(self):
        GPIO.output(self.fl_2 , GPIO.LOW)
        GPIO.output(self.fl_1 , GPIO.HIGH)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.HIGH)
        GPIO.output(self.bl_2 , GPIO.HIGH)
        GPIO.output(self.bl_1 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.HIGH)
        GPIO.output(self.br_1 , GPIO.LOW)

    def South_East(self):
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fl_2 ,  GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.HIGH)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.HIGH)
        GPIO.output(self.br_2 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.LOW)

    def South_West(self):
        GPIO.output(self.fl_2 , GPIO.HIGH)
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.HIGH)
        GPIO.output(self.bl_1 , GPIO.LOW)

    def North_East(self):
        GPIO.output(self.fl_2 , GPIO.LOW)
        GPIO.output(self.fl_1 , GPIO.HIGH)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.HIGH)

    def North_West(self):
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fl_2 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.fr_1 , GPIO.HIGH)
        GPIO.output(self.br_1 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.HIGH)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.LOW)
    def stop(self):
        GPIO.output(self.fl_1 , GPIO.LOW)
        GPIO.output(self.fl_2 , GPIO.LOW)
        GPIO.output(self.fr_1 , GPIO.LOW)
        GPIO.output(self.fr_2 , GPIO.LOW)
        GPIO.output(self.bl_1 , GPIO.LOW)
        GPIO.output(self.bl_2 , GPIO.LOW)
        GPIO.output(self.br_1 , GPIO.LOW)
        GPIO.output(self.br_2 , GPIO.LOW)

    def dispose(self):
        GPIO.cleanup()
       
    
    def pump_start(self):
        GPIO.output(self.p,GPIO.HIGH)

    def pump_stop(self):
        GPIO.output(self.p,GPIO.LOW)

    def Servo(self,angle) :
         self.pwm.ChangeDutyCycle(angle/18)

    def isObstacle(self):
        x = GPIO.input(self.ir)
        return True if x == 0 else False

