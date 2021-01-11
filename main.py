#KanuckEO
#BlueRainbo
#Qmlm
#OmaStark812

Score = 0
user = (input("what is your name?"))
print("Welcome", user)
if user == 'BlueRainbow':
      print("Oh sorry did not see you welcome Creator", user)
if user == 'KanuckEO':
      print("Oh sorry did not see you welcome Creator", user)
if user == 'Qmlm':
      print("Oh sorry did not see you welcome Creator", user)
if user == 'OmStar':
      print("Oh sorry did not see you welcome Creator", user)
yes = (input("Welcome to the Zombie adventure game would you like to start (yes)."))
if yes == 'yes':
  print("great!")
  print("I will give you a quick tour")
  print("Here is you a lone warrior you will get freinds some day")
  yes1 = (input("Would you like to start the game"))
if yes1 == 'yes':
      print("Great, lets start")
      ans1 = input("there is a wolf infront of you what do you want to do (tame him/ Kill him/ Run)")
if ans1 == 'tame him':
      print("You tried but he got mad and he killed you. Here is your Score." , Score )
if ans1 == 'Kill him':
      Score = Score + 1
      print("You killed him from long range with a spear and now you have a little bit of food. Your Score is:", Score)
      ans2 = input("You see a store and you have 2 dollars what do you do? (Go in the store/ Pass/ go armed)")
if ans2 == 'Go in the store':
      print("You went in the store but you got shot because there was a guy with a gun. Here is you Score", Score)
if ans2 == 'Pass':
      Score = Score - 1
      print("You passed and you did a bad thing because you were armed and you could have killed the man. there was a shooting there. Here is your Score", Score)
if ans2 == 'go armed':
      Score = Score + 5
      print("You went in and you saw a man with a gun so you used your bazooka and killed him. You did a good thing u saved 1000000 people. Here is your Score" , Score)
      
if ans1 == 'Run':
      print("You ran away but the wolf is faster than you and you got killed. Here is your Score.", Score )
      
