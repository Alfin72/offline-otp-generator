from datetime import datetime
import hashlib

sec_word = "alfin"
Temp_OTP = []


def get_time():
    today = datetime.now()
    time = today.strftime(r"%H%M")
    adjust_time = int(time)
    if  adjust_time%2 == 0:
        adjust_time = str(adjust_time)
        to_hash = (sec_word + adjust_time)
        print(to_hash)
        encrypt_string(to_hash)
    else:
        adjust_time+=1
        adjust_time = str(adjust_time)
        to_hash = (sec_word + adjust_time)
        print(to_hash)
        encrypt_string(to_hash)

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    sha_signature = str(sha_signature)
    Temp_OTP.append(sha_signature)

get_time()

print(Temp_OTP)