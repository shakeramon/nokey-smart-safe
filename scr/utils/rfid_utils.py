import RPi.GPIO as GPIO, time
from mfrc522 import MFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

reader = MFRC522(bus=0, device=0, pin_rst=25)

def scan_tag(timeout=0.2):
    st, _ = reader.MFRC522_Request(reader.PICC_REQIDL)
    if st == reader.MI_OK:
        st, uid = reader.MFRC522_Anticoll()
        if st == reader.MI_OK:
            return "".join(f"{b:02X}" for b in uid).upper()
    return None
