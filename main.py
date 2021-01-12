#KanuckEO
#BlueRainbo
#Qmlm
#OmaStark812

Score = 0
Money = 2
freinds = 0
Followers = 0

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
yes = (
    input("Welcome to the Text adventure game would you like to start (yes)."))
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
    ans2 = input(
        "You see a store and you have 2 dollars what do you do? (go in the store/ pass/ go armed)"
    )
if ans2 == 'go in the store':
    print(
        "You went in the store but you got shot because there was a guy with a gun. Here is you Score",
        Score)
if ans2 == 'pass':
    Score = Score - 1
    print(
        "You passed and you did a bad thing because you were armed and you could have killed the man. there was a shooting there. Here is your Score",
        Score)
if ans2 == 'go armed':
    Score = Score + 5
    print(
        "You went in and you saw a man with a gun so you used your bazooka and killed him. You did a good thing u saved 1000000 people but you didnt buy anything. Here is your Score and Money",
        Score, Money)

    ans3 = input(
        "You meet an archer. Do you want to invite him to your party but you goot to give him a dollar (invite him/ Pass on the party)"
    )
if ans3 == 'invite him':
    print(
        "you invited him and he got mad that he did not get the fruit punch he wanted and he killed you with his archering skills. Here is you Score and Money",
        Score, Money)

if ans3 == 'Pass on the party':
    print("You passed. Here is you Score and Money", Score, Money)

    ans4 = input(
        "You find a rich guy on the street and he is offering you a job to be a servent (Pass/ Take the job)"
    )

if ans4 == 'Pass':
    Score = Score + 1
    print(
        "Ok you passed but you could have gotten 1 million dollars and you are still a poor lone warrior. Here is you score Money and freinds",
        Score, Money, freinds)

    ans5 = input(
        "You are still poor, You encounter a man in a yellow suit saying that he will make you immortal(take it/ Pass)"
    )

if ans5 == 'take':
    print(
        "You are immortal and married to another immortal person but you and your partner get bored of your life"
    )

if ans5 == 'Pass':
    print(
        "You didn't drink the water and you did a good thing because you could of gotten bored from life and died after a few years"
    )

if ans4 == 'Take the job':
    Money = Money + 1000000
    Score = Score + 1
    freinds = freinds + 1
    print(
        "You got the job and you got 1000000 dollars and now you have a freind called Tom Brady and now you are a famous servent. Here is you score Money and freinds",
        Score, Money, freinds)

    ans6 = input(
        "Tom Brady died and you got a job as the CFO of Apple (accept/ Pass)")
if ans6 == 'accept':
    Money = Money + 900000000
    Score = Score + 1
    Followers = Followers + 100000000
    freinds = freinds + 99999
    print(
        "You are even richer and you are a billionaire. You get a lot of freinds and followers Here is all your criteria",
        freinds, Money, Followers, Score)
    ans7 = input(
        "You want to be the president of the US Do you want to? (yes/no)")

if ans7 == 'yes':
    Score = Score + 1
    Followers = Followers + 100000
    Money + Money + 1000
    print(
        "You took the job and you are now the President of the United States Here is all your criteria",
        freinds, Money, Followers, Score)

    Presi = input("You were rich and you were poor but you have to die one day and you did who do you want to give crown of US to")

    print("You have given the Crown of The Us to" , Presi)
    

if ans7 == 'no':
    Score = Score + 2
    Followers = Followers + 100000
    Money + Money + 1000
    print(
        "You did not take the the withe house and you are not the president but you still have a job Here is all your criteria",
        freinds, Money, Followers, Score)
    print("You also got stepped up to CEO because of the death of Tim Cook")
    CEO = input(
        "You were rich and you were poor but you have to die one day and you did who do you want to give crown of apple to"
    )

    print("You have given the Crown of Apple to", CEO)

if ans6 == 'Pass':
    print(
        "You were jobless and someone took your money you then you died from hunger"
    )

if ans1 == 'run':
    print(
        "You ran away but the wolf is faster than you and you got killed. Here is your Score.",
        Score)
