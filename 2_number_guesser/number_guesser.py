import random 

top_of_range= input("Type the number : ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <= 0:
       print("please type a number larger then 0 next time ")
       quit()
else:
    print("please type a number next time ")
    quit()


random_number = random.randint(0,top_of_range)
guess=0
# print(random_number)

while True :
   guess +=1
   user_guess = input("make a guess : ")
   if user_guess.isdigit():
      user_guess= int(user_guess)
   else:
      print("please type a number next time ")
      continue
   
   if user_guess == random_number :
      print("You got it !")
      break
   elif user_guess >random_number :
      print("you were above the number ! ")
   else:
      print("you were below the number ! ")

print("you ware ", str(guess) ," time wrong ")