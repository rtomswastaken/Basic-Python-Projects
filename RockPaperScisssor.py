import random

def score(w):
    global ps
    global bs
    if w=="P":
        ps+=1
    elif w=="B":
        bs+=1

def game():
    global ps
    global bs
    x=True
    while x:    
        opt=["R","P","S"]
        bc=random.choice(opt)
        print(bc)
        uc=input("Choose:\nR: Rock,\nP: Paper,\nS: Scissor\n(Type X to quit Game)\n\nPlayer Choice: ")

        if uc in "xX":
            x=False
            print("\nGame Ended!")
            break
        if bc==uc.upper():
            print(f"Bot Choice:{bc} \nGame Tie")
        elif bc=="R" and uc.upper()=="S":
            print(f"Bot Choice:{bc}")
            score("B")
        elif bc=="S" and uc.upper()=="P":
            print(f"Bot Choice:{bc}")
            score("B")
        elif bc=="P" and uc.upper()=="R":
            print(f"Bot Choice:{bc}")
            score("B")
        elif bc=="S" and uc.upper()=="R":
            print(f"Bot Choice:{bc}")
            score("P")
        elif bc=="P" and uc.upper()=="S":
            print(f"Bot Choice:{bc}")
            score("P")
        elif bc=="R" and uc.upper()=="P":
            print(f"Bot Choice:{bc}")
            score("P")

    print(f"Game Ended!\nScores:\nBot: {bs}\nPlayer: {ps}")
    if ps>bs:
        print("\nPlayer won!")
    elif bs>ps:
        print("\nBot won!")
    else:
        print("\nTie")

ps,bs=0,0
game()
