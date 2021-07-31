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

def game(lst_sec:list,lst_gm:list):
    hrac_vysl = [0, 0]
    for pc, hrac in zip(lst_sec, lst_gm):
        if int(hrac) in lst_sec:
            hrac_vysl[0] += 1
            if int(pc) == int(hrac):
                hrac_vysl[1] += 1


    return hrac_vysl

