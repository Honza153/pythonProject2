import sys
import help_game as gm

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

    num = gm.generCisla()
    sec_lst = gm.getCisla(num)
    #print(sec_lst)

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

    hrac = gm.game(sec_lst,lst_hrac)
    print("cows: ",hrac[0]," bulls: ",hrac[1])



if __name__ == '__main__':
    main()




