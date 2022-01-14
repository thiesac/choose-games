import random
#What should we play now?

#Ask how much time the players have

game_length = int(input("""
Choose one option 
[1]We are young and there is nothing left to do today  
[2]I´m running out of time and I still have some knitting to do 
"""))

#Long games function
if (game_length == 1):
    print("Ok, it looks like we are going to spend the rest of our lives playing...")
    with open("longgames.txt") as f:
        long_games_list = f.readlines()
        print("The winner is: ", random.choice(long_games_list))


#Short games function
elif (game_length ==2):
    print("So, you are being cheap with you time...")
    with open("shortgames.txt") as f:
        short_games_list = f.readlines()
        print("The winner is: ", random.choice(short_games_list))

else:
    print("Don´t fool me, choose a number between 1 - 2.")




