import random

def otp_password(length=4):
    return "".join(str(random.randint(0,9)) for _ in range(length))
