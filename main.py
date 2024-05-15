import level1, level2, level3, level4, level5, level6, level7, level8, level9, level10
from math import inf
from emoji import emojize
print("FRANCHISE EMOJI GUESSR 9000\n GUESS THE MOVIE, GAME, OR BOOK FROM THE EMOJI\n(some hints are decieving!)\n")

clown = emojize(":clown_face:")
strikes = 0
losses = 0

while True:
    print("losses:", losses)

    # Level 1
    while True:
        level1.level_1()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "walk the line":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue
        
    # Level 2
    while True:
        level2.level_2()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "planet of the apes":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

    # Level 3
    while True:
        level3.level_3()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "free guy":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

    
    # Level 4
    while True:
        level4.level_4()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "lord of the rings":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue


    # Level 5
    while True:
        level5.level_5()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "bone":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

    
    # Level 6
    while True:
        level6.level_6()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "the truth about chuck norris: 400 facts about the worlds greatest human" or lvlguess.lower() == "the truth about chuck norris: 400 facts about the world's greatest human":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

    # Level 7
    while True:
        level7.level_7()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "the walking dead: season 1" or lvlguess.lower() == "the walking dead: season one":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

    # Level 8
    while True:
        level8.level_8()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "super mario galaxy":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue


    # Level 9
    while True:
        level9.level_9()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "garfield kart":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

   # Level 10
    while True:
        level10.level_10()
        lvlguess = input("Guess here: ")
        if lvlguess.lower() == "madagascar":
            print("Correct!")
            break
        else:
            print("Incorrect.")
            strikes += 1
            if strikes == 3:
                print("You lose!")
                print(clown,"\n\n\n")
                losses += 1
                continue
            else:
                continue

    if losses == 0 and strikes == 0:
        break
    else:
        print("YOU SUCK! try again, and do it PERFECTLY!")
        continue

print("YOU WIN! YOU DON'T SUCK! I honestly thought\n the Chuck Norris one would've got you, but I guess not!")

