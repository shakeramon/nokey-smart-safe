from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27,
              port=1, cols=16, rows=2, dotsize=8)

def show(line1="", line2="", force=False):
    lcd.clear()
    lcd.write_string(line1[:16])
    lcd.crlf()
    lcd.write_string(line2[:16])
    time.sleep(0.05)
