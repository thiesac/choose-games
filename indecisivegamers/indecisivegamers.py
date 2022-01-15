import Image
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
    with open("longgames.txt") as f: #open txt file with list of games
        long_games_list = f.readlines() #read txt as a list
        print("The winner is: ")
        gamel = random.choice(long_games_list)  # randomly chooses the game from the list
        gamel = gamel.rstrip("\r\n")  # remove newline
        img = Image.open(gamel)  # open image of the game
        img.show(gamel)  # show image of the game



#Short games function
elif (game_length ==2):
    print("So, you are being cheap with your time...")
    with open("shortgames.txt") as f: #open txt file with list of games
        short_games_list = f.readlines() #read txt as a list
        print("The winner is: ")
        game = random.choice(short_games_list) #randomly chooses the game from the list
        game = game.rstrip("\r\n") #remove newline
        img = Image.open(game) #open image of the game
        img.show(game) #show image of the game
else:
    print("Don´t fool me, choose a number between 1 - 2.")


