import time
import sys
import random
# Number War 

def intro(): # Game intro 
    print("~~~~~~~~~~WAR~~~~~~~~~~")
    time.sleep(2)
    print("~~~RULES~~~")
    print("1. You will pick a number 1 - 10 ")
    print("2. If you pick a higher number than the computer you get that number")
    print("3. If you the computer gets the number than the computer wins")
    print("4. If you and the computer tie! It is WAR!")
    print("5. The highest card than wins, if tied again it will continue war!")
    play = input("With that being said!? Do you want to play? Y/N").lower()
    if play == 'y':
        print('Lets play then!')
        time.sleep(2)
        print("Good luck!")
        time.sleep(1)
    else: 
        print("Well that is sad!")
        time.sleep(2)
        sys.exit()

intro()

# The main game
def gameofwar():
    playertotal = 0 
    bottotal = 0  
    validnums = [1,2,3,4,5,6,7,8,10,11]
    while playertotal < 100 and bottotal < 100:
        bot = random.randint(1,10)
        try: 
            drawagain = int(input("Enter a number!"))
            if drawagain not in validnums: 
                print("That is not a valid number!")
                continue
            else:
                    print(f'The computer has drawn {bot}')
                    time.sleep(2)
                    print(f'The player has drawn {drawagain}')
                    time.sleep(2)
                    
            if drawagain == bot:
                    print("~~~~~WAR HAS STARTED!~~~~~")
                    time.sleep(2)
                    
                    while True:
                         bot_war = random.randint(1,10)
                         drawagain = (int(input("Enter a number for war!")))
                         print(f'The computer has drawn {bot_war}')
                         print(f'The player has drawn {drawagain}') 
                         if drawagain > bot_war:
                             print("The player has won this round of war!")
                             playertotal += drawagain
                             break
                         elif bot_war > drawagain:
                             print("The computer has won this round of war!")
                             bottotal += bot_war
                             break
                         else:
                             print("WAR CONTINUES")
            elif bot > drawagain: 
                print("The computer has won this round of war!")
                bottotal += bot
            else: 
                print("The player has won this round of war!")
                playertotal += drawagain

        except ValueError:
            print("That is not a number!")

        if playertotal >= 100: 
            print("~~~~~THE WAR IS OVER!~~~~~")
            time.sleep(2)
            print('The player has won the game and has reached 100')
            time.sleep(2)
            print("Good job... you beat me.")
            time.sleep(2)
            print("Until next time...")
            time.sleep(2)
            play_rematch()
            return
        elif bottotal >= 100:
            print("~~~~~THE WAR IS OVER!~~~~~")
            time.sleep(2)
            print('The computer has won the game and has reached 100')
            time.sleep(2)
            print("I have won")
            time.sleep(2)
            play_rematch()
            return


def play_rematch():
    rematch = input("Would you like a rematch? Y/N").lower()
    if rematch == 'y':
        print("Alright... so be it!")
        time.sleep(2)
        gameofwar()
    else:
        print("I see...")
        time.sleep(2)
        print("The best of wishes!")
        time.sleep(5)
        sys.exit

# Checking to make sure players number is a number or 1 - 10
while True: # Checks and runs while it is true this is for the try catch statement to make sure our user inputs a number
    try:
        global validnums
        global player
        validnums = [1,2,3,4,5,6,7,8,10,11] # Our list of valid numbers 
        player = int(input("Enter a number!")) # Users input 
        if player in validnums:
            print("Good choice")
            print(f'Player has picked {player}')
            break
        else: 
            print("That is not a valid number")
    except ValueError: # If players input is not a number it is not valid and try's the try statement until the while true condition is met 
        print("That is not a number!")

gameofwar()