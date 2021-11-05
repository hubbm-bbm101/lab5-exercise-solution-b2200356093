N= int(input("Please enter a number"))#Calculator
a= ((N//2)+1)
b= (N/2)
if (N%2)!=0:
    print(a*a)
elif (N%2==0):
    print(((N+1)*N)/b)