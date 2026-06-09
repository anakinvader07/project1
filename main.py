'''
rock paper scissor game
1 for rock
2 for paper
3 for scissor
'''
computer="rock"
dict ={
    1:"rock",
    2:"paper",
    3:"scissor"
}
n=int(input("enter number of turns:"))
u=0
pc=0 
for i in range(0,n): 
    choice=int(input("enter your choice:\n1 for rock\n2 for paper\n3 for scissor"))
    if(computer=="rock"):
        if(choice==1):
            print(f"computer chose {computer}")
            print("draw\n")
        elif(choice==2):
            print(f"computer chose {computer}")
            print("you win this round \n")
            u+=1
        else:
            print(f"computer chose {computer}")
            print("you lose this round \n")
            pc+=1
    elif(computer=="paper"):
        if(choice==2):
            print(f"computer chose {computer}")
            print("draw\n")
        elif(choice==3):
            print(f"computer chose {computer}")
            print("you win this round \n")
            u+=1
        else:
            print(f"computer chose {computer}")
            print("you lose this round \n")
            pc+=1
    else:
        if(choice==3):
            print(f"computer chose {computer}")
            print("draw\n")
        elif(choice==1):
            print(f"computer chose {computer}")
            print("you win this round \n")
            u+=1
        else:
            print(f"computer chose {computer}")
            print("you lose this round \n")
            pc+=1
if(pc==max(pc,u)): print(f"computer points:{pc}\nyour points:{u}\ncomputer won")
else: print(f"computer points:{pc}\nyour points:{u}\nyou won")