import random

computer_wins=0
user_wins=0

options =["rock","paper","scissors"]

while True:
    user_input =input("type Rock\paper\scissors and q to QUIT ").lower()
    if user_input == "q":
        print("You have quit the game")
        break
    
    if user_input not in options:
        print("PlEASE TYPE  Rock\paper\scissors and q ONLY!!!")
        continue
    
    random_number = random.randint(0,1)
    computer_pick= options[random_number]
    print("computer picked",computer_pick,".")
    
    if user_input == "rock" and computer_pick =="scissors":
        print("You won")
        user_wins +=1
        
    elif user_input == "scissors" and computer_pick =="paper":
        print("You won")
        user_wins +=1
        
    elif user_input == "paper" and computer_pick =="rock":
        print("You won")
        user_wins +=1
    
    else:
        print("You Lost")
        computer_wins +=1 
        
print("The computer has",computer_wins,"wins.")
print("You have",user_wins,"wins.")
print("Goodbye")
      
