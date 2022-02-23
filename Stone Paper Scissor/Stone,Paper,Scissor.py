import random

def gamewin(player,computer):
    if computer=="Stone":
        if player=="Paper":
            return True
        elif player=="Scissor":
            return False
        else:
            return None
    elif computer=="Paper":
        if player=="Scissor":
            return True
        elif player=="Stone":
            return False
        else:
            return None
    else:
        if player=="Stone":
            return True
        elif player=="Paper":
            return False
        else:
            return None

listelements=["Stone","Paper","Scissor"]
a="Start"
while a=="Start":
    print("Stone, Paper ,Scissor !!")
    player=input("Enter your choice :Stone ,Paper,Scissor : ").capitalize()
    computer=random.choice(listelements)
    print("You Chose : ",player)
    print("Computer Chose : ",computer)
    a=gamewin(player,computer)
    if a==None:
      print("The Game is Tied ")
    elif a==True:
      print("You Win !!")
    elif a==False:
      print("You Lose !!")
    a=input("Start Again or Exit ,Enter Start to Continue :").capitalize()
if a!="Start":
    print("Good Game !!")
