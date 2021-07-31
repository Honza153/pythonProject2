import random

def generCisla():
    while True:
        num = random.randint(1111, 9999)
        if zrus_duplicity(num):
            return num
        else:
            continue


def zrus_duplicity(num):
    if len(str(num)) == len(set(str(num))):
        return True
    else:
        return False


def getCisla(num):
    return [int(i) for i in str(num)]

