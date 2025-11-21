# nokey-smart-safe
Raspberry Pi–based smart locker system using RFID (RC522), OTP verification, servo locking, and I2C LCD display. Full hardware–software implementation for secure key-less access.

# NOKEY Smart Safe — Raspberry Pi (RFID + OTP + Keypad + Servo + LCD)

A complete Raspberry Pi–based smart locker system using RFID cards, OTP keypad verification, smooth servo-controlled locks, and an I2C LCD display.  
All assignments and releases are stored in `cases.json` for persistence.

---

## System Overview

### Assign Process (RFID)
1. User taps RFID card.  
2. LCD displays:  
   `Case X OTP:YYYY`  
   `Press case number`  
3. User presses the case number on the keypad.  
4. User enters the OTP.  
5. If correct → the case closes and is saved in `cases.json`.

Cancel anytime using `*` or `0`.

---

### Release Process (Keypad)
1. Press any keypad key to start release mode.  
2. Enter Case Number.  
3. Enter OTP.  
4. Case opens.  
5. Press `#` to close.  
6. LCD shows:  
   - Total usage time  
   - Payment amount  
7. Case is freed and removed from JSON.

Cancel anytime using `*` or `0`.

---

## Hardware Requirements

- Raspberry Pi (BCM mode)
- RC522 RFID Module (SPI)
- 4×3 Keypad
- 2 × Servos (SG-90 or MG-996R)
- 16×2 I2C LCD (PCF8574 @ 0x27)
- External 5V supply for servos (recommended)
- Common GND between Pi and servo power supply

---

## Wiring (BCM Pinout)

### RFID RC522 (SPI)
| RC522 | Raspberry Pi BCM |
|-------|------------------|
| SDA   | GPIO 8 (CE0)     |
| SCK   | GPIO 11          |
| MOSI  | GPIO 10          |
| MISO  | GPIO 9           |
| RST   | GPIO 25          |
| 3.3V  | 3.3V             |
| GND   | GND              |

### Keypad
**Rows:** `23, 17, 27, 22`  
**Columns:** `5, 6, 13`

### Servos
- Case 1 → GPIO **26**
- Case 2 → GPIO **12**

### LCD (I2C)
- SDA → GPIO 2  
- SCL → GPIO 3  
- Address = `0x27`

---

## Software Installation

### Enable I2C & SPI
```bash
sudo raspi-config
````

Enable:

* SPI
* I2C

### Install Python Packages

```bash
sudo apt update
sudo apt install python3-pip python3-dev i2c-tools
pip3 install mfrc522 RPLCD RPi.GPIO
```

### Check LCD Address

```bash
i2cdetect -y 1
```

---

## Folder Structure

```
src/
├── main_code.py
├── assign_process.py
├── release_process.py
├── cases.json
└── utils/
    ├── __init__.py
    ├── keypad_utils.py
    ├── lcd_utils.py
    ├── rfid_utils.py
    ├── servo_utils.py
    ├── otp_utils.py
    └── data_utils.py
```

---

## How to Run

```bash
cd src
python3 main_code.py
```

LCD idle display:

```
Tap Card OR
Press Key
```

---

## JSON Data Format (cases.json)

```json
{
  "1": {
    "uid": "C5C7B0AC1E",
    "otp": "5328",
    "time_assigned": "2025-11-21 21:05:12"
  },
  "2": null
}
```

---

## Troubleshooting

### Keypad double presses

* Increase debounce delay in `scan_key()`.
* Check wiring.

### LCD not updating

* Ensure correct address (0x27).
* Use `show(..., force=True)`.

### RFID not reading

* SPI enabled in raspi-config.
* RST = GPIO 25.
* BCM mode used everywhere.

### Servo jitter

* Use external 5V.
* Ground must be common.

---

## Future Improvements

* Admin mode to list active cases
* Add more lockers
* Add mobile app / Bluetooth control
* Add transaction logs
* Add encrypted storage

---

## License

MIT License

```

---

If you want this **as a downloadable README.md file**, tell me:  
**“export README as file”**
```
