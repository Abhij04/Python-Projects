import random 

user_wins =0 
computer_wins =0 
options =["rock","paper","sciessors"] 

while True :
    user_input=input("Type Rock/paper/Sciessors or Q to Quit : ").lower()
    if user_input == "q" :
        # print("game quited ")
         break 
    
    if user_input not in options :
        continue

    random_number = random.randint(0,2)
    # rock =0 , paper = 1, sciessors = 2 
    computer_pick = options[random_number]
    print("computer picked", computer_pick +".")

    if user_input == "rock" and computer_pick == "sciessors":
        user_wins += 1
        print("User Wins")
        continue

    elif(user_input == "paper" and computer_pick == "rock"):
        user_wins += 1
        print("User Wins")
        continue

    elif user_input == "sciessors" and computer_pick == "paper":
        user_wins += 1
        print("user wins")
        continue
    
    else:
        computer_wins +=1
        print("user lose !")

   
print("You win ",user_wins ,"times.")
print("computer win ",user_wins ,"times.")

print("Good Bye !")