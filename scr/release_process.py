import datetime, time
from lcd_utils import show
from servo_utils import open_case, close_case
from keypad_utils import scan_key, get_code
from data_utils import load_cases, save_cases, RATE_PER_MIN

cases = load_cases()

def release_process():
    show("Enter Case #","")
    cid = None

    # choose case
    while True:
        k = scan_key()
        if k in cases:
            cid = k
            break
        if k in ("*", "0"):
            show("Cancelled","")
            time.sleep(1)
            show("Tap Card OR","Press Key")
            return

    rec = cases[cid]
    if not rec:
        show("Case Empty","")
        time.sleep(2)
        show("Tap Card OR","Press Key")
        return

    # enter otp
    show(f"Case {cid}","Enter OTP:")
    entered = get_code(4)
    if entered.strip() != str(rec["otp"]).strip():
        show("Wrong OTP","")
        time.sleep(2)
        show("Tap Card OR","Press Key")
        return

    # open case
    open_case(cid)
    show(f"Case {cid}","Press # to close")

    # wait for close
    while True:
        k = scan_key()
        if k == "#":
            close_case(cid)
            start = datetime.datetime.strptime(rec["time_assigned"], "%Y-%m-%d %H:%M:%S")
            elapsed = max((datetime.datetime.now()-start).total_seconds()/60, 1)
            pay = round(elapsed * RATE_PER_MIN, 2)
            show(f"Time:{elapsed:.1f}m", f"Pay: ₪{pay}")
            cases[cid] = None
            save_cases(cases)
            time.sleep(3)
            show("Tap Card OR","Press Key")
            return
        if k in ("*", "0"):
            show("Cancelled","")
            return
