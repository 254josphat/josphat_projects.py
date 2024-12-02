name = input("Type your name ")
print("Welcome "+name+" to adventure to this adventure")

answer = input("You are on a dirt road it has come to an end , you can turn left or right .Which way would you like to go? ").lower()
 
if answer== "right":
    answer = input("you have come to a river , you can either cross it or walk around. Type walk/swim ").lower()
    if answer ==  "swim":
        print("You swam across the river and were eaten by crocodile")
    elif answer == "cross" :
        print(" You have crossed the Bridge.")
    else:
        print("This is nota valid option.")
      

elif answer == "left":
    answer = input("You have come a haunted house. Type Explore/ abandon. ").lower()
    if answer== "explore":
        print("You are exploring the house.")
        answer= input("You found an old lady offering a cup of coffee. type yes/no. ")
        if answer== "yes":
            print("Thank you Madam for the cup of tea.")
            print("Grandma: 'You are welcome my son.Today is a chilling morning'")
        elif answer == "no":
            print("You continue to travel deeper into the dark forest.")
        else:
            print("This is not a Valid option")
    elif answer == "abandon":
        print("You left the Haunted House")
    else:
        quit()

else:
    print("Please choose RIGHT or LEFT.")

print("Thank you for trying.Have a lovely day.")