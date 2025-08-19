import random
def rules():
    input("Welcome to Hangman!\nDeveloped by Radhil Hussain\nPress Enter")
    input("Rules:")
    input("1. You can choose difficulty level or freeplay mode where you can play with as many elements as you want")
    input("2. You can't enter total no.of.elements as 1")
    input("3. You can't enter duplicate values.")
    input("4. No.of.chances = length of element")
    input("Considering player health, we also have anti-addiction limits. Play safe")
    input("Have fun and don't cheat. We have cheat detection program\n")
    
def cheat(c):
    if(c==1):
        print("But you cheated!")
        
def hangman():
    c=0
    words=[]
    d=int(input("Choose Difficulty Level (0,1,2,3):\n0=Easy\n1=Medium\n2=Hard\n3=Freeplay\n"))
    if (d==0):
        d1=3;
    elif (d==1):
        d1=5;
    elif (d==2):
        d1=7;
    else:
        d1=int(input("Enter no.of.elements: "))
    n1=d1
    if(n1==1):
        print("This is cheating. Play with more elements")
        n3=int(input("Add more elements: "))
        if (n3==0):
            c=1
        n1+=n3
    for i in range(n1):
        print("Enter word",i+1,": ")
        ele=str(input())
        ele.upper()
        if (ele in words):
            ele=str(input("Enter a different element: ").upper())
            if (ele in words):
                ele=str(input("I said,'A different element'!: ").upper())
                if (ele in words):
                    c=1
                    print("Fine!")
                    words.append(ele.upper())
                else:
                    words.append(ele.upper())
            else:
                words.append(ele.upper())
        else:
            words.append(ele.upper())
    
    t = random.choice(words).strip()
    n = len(t)
    guessedLetters = set()
    numGuessedLetters = 0
    
    gameStrList = [
        "_",
    ] * len(t)
    
    print(" ", "_" * n)
    for i in range(n):
        print("Chances left: ",n-i)
        s = input("| Guess?(case insensitive) ").upper()
        if(s==t):
            numGuessedLetters=len(t)
            print(t)
            break
        for i, ch in enumerate(t):
            if s == ch and s not in guessedLetters:
                gameStrList[i] = s
                numGuessedLetters += 1
        guessedLetters = set(gameStrList)
        print("".join(gameStrList).center(n + 4))
        gameOver = numGuessedLetters == len(t)
    
    if(numGuessedLetters!=len(t)):
        print("You lost!")
    else:
        print("You win!")
    cheat(c)
    print("Game over!\n")

def run():   
    n2=0
    rules()
    while True:
        hangman()
        n2+=1
        ch=str(input("Do you want to continue? (y/n): "))
        if(ch=="y" or ch=="Y"):
            print("\n")
        else:
            print("Thank You!")
            break
        if(n2==5):
            print("You've been playing for a long time. Game closed")
            break
        
run()