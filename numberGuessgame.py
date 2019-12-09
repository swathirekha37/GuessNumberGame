import random

def NumGame():
    count=1
    compnum=random.randint(1,100)
    userguess = int(input("enter a num between 1 and 100:"))
    f=1

    while count<10:

        if userguess<compnum:
            print "guess is too low"
            count = count + 1
            userguess = int(input("enter a num between 1 and 100:"))
        elif userguess>compnum:
            print "guess is too high"
            count = count + 1
            userguess = int(input("enter a num between 1 and 100:"))
        elif userguess==compnum:
            print "you won the game!"
            print "computernum is "+str(compnum)
            f=0
            break
        else:
            print "this is invalid number. please try agian"
            continue

    if f==1:
        print "oops you are out of chance and lost the game."

    print ""

def main():
    NumGame()
    while True:
        option=str(input("do you want to play again? (y/n): "))
        if option=='y':
            NumGame()
        else:
            print "Thank you for playing!. Come back soon!"
            break


main()