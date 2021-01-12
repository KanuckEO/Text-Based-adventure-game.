#KanuckEO
#BlueRainbo
#Qmlm
#OmaStark812

Score = 0
Money = 2

user = (input("What is your name"))
print("Welcome", user)
if user == 'BlueRainbow':
    print("Oh sorry did not see you welcome Creator", user)
if user == 'KanuckEO':
    print("Oh sorry did not see you welcome Creator", user)
if user == 'Qmlm':
    print("Oh sorry did not see you welcome Creator", user)
if user == 'OmaStar':
    print("Oh sorry did not see you welcome Creator", user)
yes = (input(
    "Welcome to the Text adventure game would you like to start (yes)."))
if yes == 'yes':
    print("great!")
    print("I will give you a quick tour")
    print("Here is you a lone warrior you will get freinds some day")
    yes1 = (input("Would you like to start the game"))
if yes1 == 'yes':
    print("Great, lets start")
    ans1 = input(
        "there is a wolf infront of you what do you want to do (tame him/ kill him/ run)"
    )
if ans1 == 'tame him':
    print("You tried but he got mad and he killed you. Here is your Score.",
          Score)
if ans1 == 'kill him':
    Score = Score + 1
    print(
        "You killed him from long range with a spear and now you have a little bit of food. Your Score is:",
        Score)
    ans2 = input("You see a store and you have 2 dollars what do you do? (go in the store/ pass/ go armed)")
if ans2 == 'go in the store':
    print("You went in the store but you got shot because there was a guy with a gun. Here is you Score", Score)
if ans2 == 'pass':
    Score = Score - 1
    print("You passed and you did a bad thing because you were armed and you could have killed the man. there was a shooting there. Here is your Score",Score)
if ans2 == 'go armed':
    Score = Score + 5
    print("You went in and you saw a man with a gun so you used your bazooka and killed him. You did a good thing u saved 1000000 people but you didnt buy anything. Here is your Score and Money",Score, Money)
        
    ans3 = input("You meet an archer. Do you want to invite him to your party but you goot to give him a dollar (invite him/ Pass on the party)")
if ans3 == 'invite him':
    print("you invited him and he got mad that he did not get the fruit punch he wanted and he killed you with his archering skills. Here is you Score and Money", Score, Money)

if ans3 == 'Pass on the party':
    print("You passed. Here is you Score and Money", Score, Money)
  
    ans4 = input("You find a rich guy on the street and he is offering you a job to be a servent (Pass/ Take the job)")

if ans4 == 'Pass':
    Score = Score + 1
    print("Ok you passed but you could have gotten 1 million dollars and you are still a poor lone warrior")

if ans4 == 'Take the job':
    Money = Money + 1000000
    Score = Score + 1
    print("You got the job and you got 1000000 dollars and now you have a freind called Tom Brady and now you are a famous servent.")

if ans1 == 'run':
    print("You ran away but the wolf is faster than you and you got killed. Here is your Score.",Score)
