name =input("Enter your Name : ")
print("welcome ", name,"to this adventure!" )

answer = input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go ? ").lower()

if answer == "left" :
    answer=input("you come to a river, you can walk around it or swim across? type walk to walk around and swim to swim accross : ").lower()

    if answer == "swim" :
        print("you swim across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for a many miles , ran out of water and you dead !")
    else:
        print("Nota valid option. you lose !")

elif answer=="right":
    answer = input("you come to a brige, it looks wobbly , do you want to cross it or head back ?(cross/back) ").lower()
    if answer == "swim" :
        print("you swim across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked for a many miles , ran out of water and you dead !")
    else:
        print("Nota valid option. you lose !")

else:
    print("Nota valid option. you lose !")