import json, os

CASES_FILE = "cases.json"
NUM_CASES = 2
RATE_PER_MIN = 1.0  # ₪ per minute

def reset_cases():
    data = {str(i): None for i in range(1, NUM_CASES+1)}
    with open(CASES_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return data

def load_cases():
    try:
        with open(CASES_FILE) as f:
            return json.load(f)
    except:
        return reset_cases()

def save_cases(cases):
    if os.path.exists(CASES_FILE):
        os.replace(CASES_FILE, CASES_FILE + ".bak")
    with open(CASES_FILE, "w") as f:
        json.dump(cases, f, indent=2)

def first_free_case(cases):
    for cid, rec in cases.items():
        if rec is None:
            return cid
    return None
