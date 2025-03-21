print("welcome to my Python Quiz ! ")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes" :
  quit()

print("okay ! Let's play :)")
score = 0

answer=input("what is the full from of CPU ? ")
if answer.lower() == "central processing unit" :
  print('correct!')
  score += 1
else:
  print("Incorrect!")

answer=input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
  print('correct!')
  score += 1
else:
  print("Incorrect!")

answer=input("what does RAM stand for? ")
if answer.lower() == "random access memory" :
  print('correct!')
  score += 1
else:
  print("Incorrect!")

answer=input("what does PSU stand for? ")
if answer.lower() == "power supply" :
  print('correct!')
  score += 1
else:
  print("Incorrect!")

print("you got " + str(score) +" questions correct !")
print("you got " + str((score/4)*100) +" percentage !")

 