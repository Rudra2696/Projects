print("Welcome to tic tac toe game")

try:
    a=input("Enter name of 1st player : ")
    a=a.capitalize().strip()
except(ValueError,SyntaxError,TypeError):
        print("Something went wrong!!")               

try:
    b=input("Enter name of 2nd player : ")
    b=b.capitalize().strip()
except(ValueError,SyntaxError,TypeError):
        print("Something went wrong!!")


print("""

1 | 2 | 3
----------      
4 | 5 | 6
----------      
7 | 8 | 9


""")

print(f"For O Enter 1\n For X Enter 2")

while True:
    try:
        n=int(input(f"What is your choice {a} for the game (1/2): "))     
        if (n==1 or n==2):
            break
        else:
            print("Enter 1/2 only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")


if n==1:
    z="O" 
    y="X"
else:
    z="X" 
    y="O"

print(f"{a} you choose {z} \n {b} you choose {y}")    

p="""

1 | 2 | 3
----------      
4 | 5 | 6
----------      
7 | 8 | 9


"""
l=[1,2,3,4,5,6,7,8,9]

while True:
    try:
        n1=int(input(f"where do you want to place your choice {a} : "))     
        if (n1==1 or n1==2 or n1==3 or n1==4 or n1==5 or n1==6 or n1==7 or n1==8 or n1==9 ):
            break
        else:
            print("Enter 1/2/3/4/5/6/7/8/9 only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")   

p=p.replace(str(n1),f"{z}")        

print(p)

l.remove(n1)

while True:
    try:
        n2=int(input(f"where do you want to place your choice {b} : "))     
        if n2 in l:
            break
        else:
            print(f"Enter{l} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  