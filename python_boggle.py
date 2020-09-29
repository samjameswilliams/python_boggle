"""
Created on Thu Sep 24 19:59:11 2020

@author: Sam Williams

Python Boggle

"""

#   Create lists of all the letters on all the die
#   Each die numbered sequentially d1, d2 etc
d1 = ["X","L","D","E","I","R"]
d2 = ["E","H","N","E","W","G"]
d3 = ["A","E","A","N","E","G"]
d4 = ["T","A","O","T","O","W"]
d5 = ["I","E","S","N","E","U"]
d6 = ["L","V","E","R","D","Y"]
d7 = ["T","U","I","C","O","M"]
d8 = ["P","K","A","F","F","S"]
d9 = ["P","O","H","C","S","A"]
d10 = ["Qu","N","M","I","H","U"]
d11 = ["R","V","T","H","W","E"]
d12 = ["D","S","Y","I","T","T"]
d13 = ["A","J","B","O","O","B"]
d14 = ["N","Z","N","R","H","L"]
d15 = ["L","R","Y","T","E","T"]
d16 = ["S","E","I","T","O","S"]

#   Create a list containing all the die 
d_l = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]

import random
import time

#   Create die class
class Die:
    
    # Each die has attributes of its own letters
    def __init__(self, die_let):
        self.die_let = die_let
    
    # Create a method for rolling the die to get a random letter
    def roll(self):
        self.n = random.randint(0,5)
        self.roll = self.die_let[self.n]
        return self.roll

#   Create all the die objects needed for the game with a for loop

d_lo = []

for i in range(16):
    d_lo.append(Die(d_l[i]))

#   Tests to see if d_lo list has been created as desired
#print(d_lo[0].die_let)
#print(d_lo[0].roll())
#print(d_lo[15].die_let)
#print(d_lo[15].roll())


#   Print board function definition 

def prt_bd():

    #   Create all the die objects needed for the game with a for loop

    d_lo = []

    for i in range(16):
        d_lo.append(Die(d_l[i]))

    #   Shuffle the die
    
    random.shuffle(d_lo)
    
    #   Ask for length of round
    t = int(input("Input round time in seconds: "))
    
    #   Print the board
    
    print("-----------------")
    print("|",d_lo[0].roll(),"|",d_lo[1].roll(),"|",d_lo[2].roll(),"|",d_lo[3].roll(),"|")
    print("-----------------")
    print("|",d_lo[4].roll(),"|",d_lo[5].roll(),"|",d_lo[6].roll(),"|",d_lo[7].roll(),"|")
    print("-----------------")
    print("|",d_lo[8].roll(),"|",d_lo[9].roll(),"|",d_lo[10].roll(),"|",d_lo[11].roll(),"|")
    print("-----------------")
    print("|",d_lo[12].roll(),"|",d_lo[13].roll(),"|",d_lo[14].roll(),"|",d_lo[15].roll(),"|")
    print("-----------------",end='\n')
    
    #   Start the timer
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print("Time's up!","\a")

#   Welcome message

print("Welcome to Python Boggle!")
time.sleep(2)
while True:
    choice = input("Please enter 'p' to play or 'q' to quit: ")
    if choice == "p":
        prt_bd()
    elif choice == "q":
        break
    else:
        print("Invalid selection, please enter 'p' to play or 'q' to quit: ")
        
#   Test to see if die are being randomly rearranged as desired
#print(d_lo[0].die_let)