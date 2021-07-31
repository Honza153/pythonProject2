import random
import help_game

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




if __name__ == '__main__':
    main()




