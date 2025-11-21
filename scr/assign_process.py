import datetime, time
from lcd_utils import show
from otp_utils import otp_password
from servo_utils import open_case, close_case
from keypad_utils import scan_key, get_code
from data_utils import load_cases, save_cases, first_free_case

cases = load_cases()

def assign_process(uid):
    case_id = first_free_case(cases)
    if not case_id:
        show("No Free Cases","Try Later")
        time.sleep(2)
        show("Tap Card OR","Press Key")
        return

    otp = otp_password()
    show(f"Case {case_id} OTP:{otp}", "Press case number")
    open_case(case_id)

    # wait for case number
    while True:
        k = scan_key()
        if k == case_id: break
        if k in ("*", "0"):
            show("Cancelled","")
            close_case(case_id)
            time.sleep(1)
            show("Tap Card OR","Press Key")
            return

    # enter otp
    entered = get_code(4)
    if entered.strip() == str(otp).strip():
        cases[case_id] = {
            "uid":uid,
            "otp":str(otp),
            "time_assigned":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_cases(cases)
        show("Case Saved","Closing...")
    else:
        show("Wrong OTP","Closing...")

    close_case(case_id)
    time.sleep(2)
    show("Tap Card OR","Press Key")
