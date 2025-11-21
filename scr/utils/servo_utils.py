import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

CASE_PINS = {"1":26, "2":12}
GPIO.setup(CASE_PINS["1"], GPIO.OUT)
GPIO.setup(CASE_PINS["2"], GPIO.OUT)

servo1 = GPIO.PWM(CASE_PINS["1"], 50)
servo2 = GPIO.PWM(CASE_PINS["2"], 50)
servo1.start(0)
servo2.start(0)

servo_angles = {"1":0, "2":0}

def duty(angle):
    return 2.0 + (angle / 18.0)

def move_servo_smooth(servo, start_angle, end_angle, step=1, delay=0.03):
    direction = 1 if end_angle > start_angle else -1
    for a in range(start_angle, end_angle + direction, direction*step):
        servo.ChangeDutyCycle(duty(a))
        time.sleep(delay)
    servo.ChangeDutyCycle(0)

def open_case(cid):
    servo = servo1 if cid=="1" else servo2
    move_servo_smooth(servo, servo_angles[cid], 90)
    servo_angles[cid] = 90

def close_case(cid):
    servo = servo1 if cid=="1" else servo2
    move_servo_smooth(servo, servo_angles[cid], 0)
    servo_angles[cid] = 0

def cleanup_servos():
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
