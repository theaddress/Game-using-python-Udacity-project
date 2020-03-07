import time
import random


def print_pause(s, num):
    print(s)
    time.sleep(num)


def intro():
    print_pause("Your are the little red riding hood", 2)
    print_pause("You need to deliver the lunch to your " +
                "grandmother near town", 2)
    print_pause("There are two ways to grandmother town " +
                "short way accross the forest and long way", 2)


def choise():
    en = ["wolf", "Thief", "Lion", "Zombie", "Vampire"]
    enemies = random.choice(en)
    wp = ["sword", "Gun", "digger"]
    weapon = random.choice(wp)
    pz = ["1+1", "3-1", "2^1"]
    puzzle = random.choice(pz)
    print_pause("", 2)
    ch = input("""Enter 1 to choise the short way accross the forest
    \nEnter 2 choise long way\n""")
    if ch == "1":
        forest(enemies, weapon)
    elif ch == "2":
        long_way(puzzle)
    else:
        print_pause("please enter 1 or 2 only", 2)
        choise()


def forest(enemies, weapon):
    print_pause("You choose to go accross the forest", 2)
    print_pause(f"in the middle of forest you found {enemies}", 2)
    print_pause(f"You check your bag you found {weapon}", 2)
    ch2 = input("Enter 1 to fight or 2 to run away\n")
    if ch2 == "1":
        print_pause(f"you took your {weapon} for your bag", 2)
        print_pause(f"you defeat {enemies}!!!", 2)
        print_pause("you reach save to your grandmother :)", 2)
        Game_over()
    elif ch2 == "2":
        print_pause("you choose to run away", 2)
        print_pause(f"The {enemies} run after you", 2)
        print_pause(f"The {enemies} cought you and eat you :(", 2)
        Game_over()
    else:
        print_pause("please enter 1 or 2 only", 2)
        forest(enemies, weapon)


def long_way(puzzle):
    print_pause("You choose the long way", 2)
    print_pause("wise man have puzzle to accross the road", 2)
    print_pause(f"The puzzle is {puzzle}", 2)
    ans = input("Enter the solution\n")
    if ans == "2":
        print_pause("it is correct answer you allow to accross", 2)
        print_pause("you reach save to your grandmother :)", 2)
        Game_over()
    else:
        print_pause("it is not corret answer you are not allow to accross", 2)
        ch3 = input("Enter 1 for second chance \nEnter 2 for new start\n")
        if ch3 == "1":
            long_way(puzzle)
        elif ch3 == "2":
            choise()
        else:
            print_pause("please enter 1 or 2 only", 2)
            print_pause("you will go to the start of road", 2)
            long_way(puzzle)


def Game_over():
    print_pause("<<<Game over>>>", 2)
    ans1 = input("Do you want to play again?(Y/N)").lower()
    if ans1 == "y":
        play_game()
    elif ans1 == "n":
        print_pause("Game End", 1)
    else:
        print_pause("please enter Y or N only", 2)
        Game_over()


def play_game():
    intro()
    choise()


if __name__ == "__main__":
    play_game()
