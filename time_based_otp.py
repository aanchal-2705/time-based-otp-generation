import pyotp
from timeit import default_timer as timer

#base32 secret key-> 32 characters are used while generating this private key
#length of this key is 16

#32 characters --> A-Z(only uppercase) and 2-7
# space -- for per character , there is a space of 5 bits.
#total memory space -> 160 bit --> 20 bytes

with open('secret_key.txt','r') as rf:
    base_32_secret_key = rf.read()
#print(base_32_secret_key)

#otp generation

timebasedotp = pyotp.TOTP(base_32_secret_key)
current_otp = timebasedotp.now()
#print(current_otp)
def verification(time_gap, entered_otp, otp, timebasedotp):
    if (time_gap) < 30 and (entered_otp == otp):
        print("Hello user u are successfully verified")
        return
    elif (time_gap) < 30 and (entered_otp != otp):
        print("incorrecr.resend otp")
        resend_otp(timebasedotp)
    elif (time_gap) >= 30:
        print("time up!")
        resend_otp(timebasedotp)


def resend_otp(timebasedotp):
    current_otp = timebasedotp.now()
    while True:
        new_current_otp = timebasedotp.now()
        if new_current_otp != current_opt:
            print(f'Current otp: {new_current_otp}')
            start = timer()
            enter_otp = input("enter otp: ")
            end = timer()
            resend_time_interval = end - start
            print(f'time taken: {resend_time_interval}')
            verification(resend_time_interval, enter_otp, new_current_otp, timebasedotp)
            break
            return


while True:
    new_current_otp = timebasedotp.now()
    if new_current_otp != current_otp:
        print(f'current_otp: {new_current_otp}')
        start = timer()
        enter_otp = input("enter current otp: ")
        end = timer()

        time_interval = end - start
        print(f"time taken: :{time_interval}")
        verification(time_interval, enter_otp, new_current_otp, timebasedotp)
        break
