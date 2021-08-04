import sys
import random

print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
""")

def main():

    num = generCisla()
    sec_lst = getCisla(num)
    print(sec_lst)

    hrac_cislo = input("Zadej 4 místné číslo: ")
    lst_hrac = list(hrac_cislo)


    if len(lst_hrac) != 4:
        print("Zadal jsem nevhodnou délu čísla")
        sys.exit(-1)
    elif not hrac_cislo.isdigit():
        print("Číslo obsahuje nepovolené znaky")
        sys.exit(-2)
    elif int(lst_hrac[0]) == 0:
        print("Číslo nesmí začínat nulou")
        sys.exit(-3)

    hrac = game(sec_lst,lst_hrac)
    print("cows: ",hrac[0]," bulls: ",hrac[1])

# ---------------------------------------------------------------------

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


if __name__ == '__main__':
    main()




