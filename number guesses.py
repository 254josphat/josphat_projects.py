import random
top_number = input("please enter a number ")
if top_number.isdigit():
    top_number = int(top_number)
    if top_number <=0:
        print("please enter a number larger than zero nxt time")
        quit()
else:
    print("please type a number next time")
    quit()
    

random_number= random.randint(0,top_number)
guesses =0
while True:
    guesses +=1
    user_number = input("make a guess ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <=0:
            print("please enter a number larger than zero nxt time")
            quit()
    else:
        print("please type a number next time")
        quit()
    if user_number == random_number:
        print("YOU WIN!!! IN",guesses,"guesses")
        break
    else:
        if user_number > random_number:
           print("You were above the number")
        else:
            print("You were below the number") 
        print("YOU LOST. PLEASE TRY AGAIN!!!")

    