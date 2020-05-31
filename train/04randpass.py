import random
import string


def ran_pass(num=8):
    stra = string.ascii_letters + string.digits
    passb = ""
    for i in range(num):
        passa = random.choice(stra)
        passb += passa
    return passb


if __name__ == "__main__":
    data = ran_pass(10)
    print(data)
