import RPi.GPIO as GPIO, time
from lcd_utils import show

ROW_PINS = [23,17,27,22]
COL_PINS = [5,6,13]
KEYPAD_MAP = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"],
    ["*","0","#"]
]

last_key = None
last_time = 0

def setup_keypad():
    for r in ROW_PINS:
        GPIO.setup(r, GPIO.OUT)
        GPIO.output(r, GPIO.LOW)
    for c in COL_PINS:
        GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def scan_key(debounce=0.05, repeat_block=0.3):
    global last_key, last_time
    for i,r in enumerate(ROW_PINS):
        GPIO.output(r, GPIO.HIGH)
        for j,c in enumerate(COL_PINS):
            if GPIO.input(c)==GPIO.HIGH:
                key = KEYPAD_MAP[i][j]
                now = time.time()
                if key == last_key and (now - last_time) < repeat_block:
                    GPIO.output(r, GPIO.LOW)
                    return None
                last_key, last_time = key, now
                while GPIO.input(c)==GPIO.HIGH:
                    time.sleep(debounce)
                GPIO.output(r,GPIO.LOW)
                return key
        GPIO.output(r,GPIO.LOW)
    return None

def get_code(length=4, show_func=show):
    code = ""
    show_func("Enter OTP:", "", force=True)
    while len(code) < length:
        k = scan_key()
        if not k:
            continue
        if k == "*":
            code = code[:-1]
        elif k == "#":
            break
        else:
            code += k
        show_func("Enter OTP:", "*" * len(code), force=True)
    return code
