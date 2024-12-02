print ("Welcome to my game")

playing = input("DO you want to play the game? ")

if playing.lower() != "yes" :
    quit()

print("Okay Let Play:")
score = 0

answer = input ("What does CPU  stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer = input ("What does GPU  stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct")
    score +=1
else:
    print("Incorrect")

answer = input ("What does RAM  stand for? ")
if answer.lower()== "random access memory":
    print("Correct")
    score +=1
else:
    print("Incorrect")

if score ==3: 
    print ("you got "+str(score/3*100)+" out of three questions. EXCELLENT!")
else:
    print("you got "+str(score/3*100)+"% !!. yesPlay more to increase your IQ")
    