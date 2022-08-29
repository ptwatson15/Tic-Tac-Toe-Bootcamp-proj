import random

from custom_pkg import comparison

#TODO:
# Check things work properly
# Add other ways to type


def Start_of_Game():
    Standard_Or_Sheldon = input("Pick One:\n1.Standard Game\n2.Sheldon Style\n")
    print("")
    Player_Count = input("How Many Players? \n(Choose 1 or 2)\n")
    print("")
    Game_Options = ["Rock", "Paper","Scissors","Lizard","Spock"]


    #1 and Standard
    if((Standard_Or_Sheldon == "1")|(Standard_Or_Sheldon.upper() == "STANDARD")|(Standard_Or_Sheldon.upper() == "STANDARD GAME")|(Standard_Or_Sheldon.upper() == "ONE"))&((Player_Count == "1")|(Player_Count.upper() == "ONE")):
        print("Choose Between the following:")
        print(Game_Options[0:3])
        Player_Choice = input("Option Picked: ")
        print("")
        if Player_Choice.upper() in (x.upper() for x in Game_Options[-2:]):
            print("This isnt Sheldon Style")
        elif Player_Choice.upper() not in (x.upper() for x in Game_Options):
            print("Option not available")
        else:
            Computer_Choice = random.choice(Game_Options[0:3])

            print("Computer picked:",Computer_Choice)

            Compare = comparison.compare_choice(Player_Choice,Computer_Choice)
            print("")
            if(Compare == "P1"): print("You Win!")
            elif(Compare == "P2"):  print("Computer Wins!")
            elif(Compare == "TIE"):  print("TIE!")
        print()
        Start_of_Game()
            
    #1 and Sheldon
    elif((Standard_Or_Sheldon == "2")|(Standard_Or_Sheldon.upper() == "SHELDON")|(Standard_Or_Sheldon.upper() == "SHELDON STYLE")|(Standard_Or_Sheldon.upper() == "TWO"))&((Player_Count == "1")|(Player_Count.upper() == "ONE")):
        print("Choose Between the following:")
        print(Game_Options)
        Player_Choice = input("Option Picked: ")

        print("")

        Computer_Choice = random.choice(Game_Options)

        print("Computer picked:",Computer_Choice)

        Compare = comparison.compare_choice(Player_Choice,Computer_Choice)
        print("")
        if(Compare == "P1"): print("You Win!")
        elif(Compare == "P2"):  print("Computer Wins!")
        elif(Compare == "TIE"):  print("TIE!")
        print()
        Start_of_Game()
    #2 and Standard 
    elif((Standard_Or_Sheldon == "1")|(Standard_Or_Sheldon.upper() == "STANDARD")|(Standard_Or_Sheldon.upper() == "STANDARD GAME")|(Standard_Or_Sheldon.upper() == "ONE"))&((Player_Count == "2")|(Player_Count.upper() == "TWO")):
        print("Choose Between the following:")
        print(Game_Options[0:3])
        Player_1_Choice = input("Player 1 Picked: ")

        print("")

        if Player_1_Choice.upper() in (x.upper() for x in Game_Options[-2:]):
            print("This isnt Sheldon Style")
        elif Player_1_Choice.upper() not in (x.upper() for x in Game_Options):
            print("Option not available")
        else:

            print("Choose Between the following:")
            print(Game_Options[0:3])
            Player_2_Choice = input("Player 2 Picked: ")
            if Player_2_Choice.upper() in (x.upper() for x in Game_Options[-2:]):
                print("This isnt Sheldon Style")
            elif Player_2_Choice.upper() not in (x.upper() for x in Game_Options):
                print("Option not available")
            else:
                Compare = comparison.compare_choice(Player_1_Choice,Player_2_Choice)
                print("")
                if(Compare == "P1"): print("Player 1 Wins!")
                elif(Compare == "P2"):  print("Player 2 Wins!")
                elif(Compare == "TIE"):  print("TIE!")
            print()
            Start_of_Game()

    #2 and Sheldon
    elif((Standard_Or_Sheldon == "2")|(Standard_Or_Sheldon.upper() == "SHELDON")|(Standard_Or_Sheldon.upper() == "SHELDON STYLE")|(Standard_Or_Sheldon.upper() == "TWO"))&((Player_Count == "2")|(Player_Count.upper() == "TWO")):
        print("Choose Between the following:")
        print(Game_Options)
        Player_1_Choice = input("Player 1 Picked: ")

        print("")

        print("Choose Between the following:")
        print(Game_Options)
        Player_2_Choice = input("Player 2 Picked: ")

        Compare = comparison.compare_choice(Player_1_Choice,Player_2_Choice)
        print("")
        if(Compare == "P1"): print("Player 1 Wins!")
        elif(Compare == "P2"):  print("Player 2 Wins!")
        elif(Compare == "TIE"):  print("TIE!")
        print()
        Start_of_Game()

Start_of_Game()