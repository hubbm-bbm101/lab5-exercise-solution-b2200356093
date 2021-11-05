x= int(input("Welcome the  Guessing Game! Please enter a random number!:"))#Guessing game
r= 39
while True:
    if x==r :
        print("MATCHED!!")
        break
    elif x<r:
        x=int(input("Increase your number!!!"))

    elif x>r:
        x=int(input("Decrease your number!!!"))