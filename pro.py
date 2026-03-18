import random

computer=random.choice([-1,0,1])
you = (input("Enter your choice: "))
          
dict={"s":1,"w":-1,"g":0}
reversedict={1:"s",-1:"w",0:"g"}
you=dict[you]
print(f"Computer choice is {reversedict[computer]}")
print(f"Your choice is {reversedict[you]}")
if(computer==you):
    print("It's a tie")

else:
    if(computer==-1 and you ==1):
             print("You win")

    elif(computer==-1 and you ==-0):
            print("Computer wins")


    if(computer==1 and you ==1):
            print("you lose")


    elif(computer==1 and you ==0):
            print("you win")

    if(computer==0 and you ==-1):
            print("you win")

    elif(computer==0 and you ==1):      
            print("you lose")
                


