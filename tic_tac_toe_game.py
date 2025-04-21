def player1(d,a):
    list1=d
    w1=[1,2,3]
    w2=[4,5,6]
    w3=[7,8,9]
    w4=[1,4,7]
    w5=[2,5,8]
    w6=[3,6,9]
    w7=[1,5,9]
    w8=[3,5,7]    
    if all(num in list1 for num in w1):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
    elif all(num in list1 for num in w2):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()  
    elif all(num in list1 for num in w3):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
    elif all(num in list1 for num in w4):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
    elif all(num in list1 for num in w5):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
    elif all(num in list1 for num in w6):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
    elif all(num in list1 for num in w7):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
    elif all(num in list1 for num in w8):
        print(f"Congratulations !! {a}\nYou won the game")  
        exit()
      
def player2(d,b):
    list2=d
    w1=[1,2,3]
    w2=[4,5,6]
    w3=[7,8,9]
    w4=[1,4,7]
    w5=[2,5,8]
    w6=[3,6,9]
    w7=[1,5,9]
    w8=[3,5,7]    
    if all(num in list2 for num in w1):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w2):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w3):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w4):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w5):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w6):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w7):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()
    elif all(num in list2 for num in w8):
        print(f"Congratulations !! {b}\nYou won the game")  
        exit()    

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
l=["1/","2/","3/","4/","5/","6/","7/","8/","9"]
l1=[1,2,3,4,5,6,7,8,9]
list1=[]
list2=[]

z1=""    

for _ in l:
    z1=z1+f"{_}"

while True:
    try:
        n1=int(input(f"where do you want to place your choice {a} : "))     
        if n1 in l1:
            break
        else:
            print(f"Enter {z1} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")   

p=p.replace(str(n1),f"{z}")    

list1.append(n1)

print(p)

player1(list1,a)

if n1==9:
   l.remove(f"{n1}")
   l1.remove(n1)
else:
    l.remove(f"{n1}/")  
    l1.remove(n1) 

z2=""    

for _ in l:
    z2=z2+f"{_}"    


while True:
    try:
        n2=int(input(f"where do you want to place your choice {b} : "))     
        if n2 in l1:
            break
        else:
            print(f"Enter {z2} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n2),f"{y}")        

list2.append(n2)

print(p)

player2(list2,b)

if n2==9:
   l.remove(f"{n2}")
   l1.remove(n2)
else:
    l.remove(f"{n2}/")  
    l1.remove(n2) 

z3=""    

for _ in l:
    z3=z3+f"{_}"        

while True:
    try:
        n3=int(input(f"where do you want to place your choice {a} : "))     
        if n3 in l1:
            break
        else:
            print(f"Enter {z3} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n3),f"{z}")        

list1.append(n3)

print(p)

player1(list1,a)

if n3==9:
   l.remove(f"{n3}")
   l1.remove(n3)
else:
    l.remove(f"{n3}/")  
    l1.remove(n3) 

z4=""    

for _ in l:
    z4=z4+f"{_}"  

while True:
    try:
        n4=int(input(f"where do you want to place your choice {b} : "))     
        if n4 in l1:
            break
        else:
            print(f"Enter {z4} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n4),f"{y}")        

list2.append(n4)

print(p)

player2(list2,b)

if n4==9:
   l.remove(f"{n4}")
   l1.remove(n4)
else:
    l.remove(f"{n4}/")  
    l1.remove(n4) 

z5=""    

for _ in l:
    z5=z5+f"{_}"


while True:
    try:
        n5=int(input(f"where do you want to place your choice {a} : "))     
        if n5 in l1:
            break
        else:
            print(f"Enter {z5} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n5),f"{z}")        

list1.append(n5)

print(p)

player1(list1,a)

if n5==9:
   l.remove(f"{n5}")
   l1.remove(n5)
else:
    l.remove(f"{n5}/")  
    l1.remove(n5) 

z6=""    

for _ in l:
    z6=z6+f"{_}"

while True:
    try:
        n6=int(input(f"where do you want to place your choice {b} : "))     
        if n6 in l1:
            break
        else:
            print(f"Enter {z6} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n6),f"{y}")        

list2.append(n6)

print(p)

player2(list2,b)

if n6==9:
   l.remove(f"{n6}")
   l1.remove(n6)
else:
    l.remove(f"{n6}/")  
    l1.remove(n6) 

z7=""    

for _ in l:
    z7=z7+f"{_}"    


while True:
    try:
        n7=int(input(f"where do you want to place your choice {a} : "))     
        if n7 in l1:
            break
        else:
            print(f"Enter {z7} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n7),f"{z}")        

list1.append(n7)

print(p)

player1(list1,a)   

if n7==9:
   l.remove(f"{n7}")
   l1.remove(n7)
else:
    l.remove(f"{n7}/")  
    l1.remove(n7) 

z8=""    

for _ in l:
    z8=z8+f"{_}"    

while True:
    try:
        n8=int(input(f"where do you want to place your choice {b} : "))     
        if n8 in l1:
            break
        else:
            print(f"Enter {z8} only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")  

p=p.replace(str(n8),f"{y}")        

list2.append(n8)

print(p)

player2(list2,b)

if n8==9:
   l.remove(f"{n8}")
   l1.remove(n8)
else:
    l.remove(f"{n8}/")  
    l1.remove(n8) 

z9=""    

for _ in l:
    z9=z9+f"{_}"  

n9=l1[0]  

p=p.replace(str(n9),f"{z}")        

list1.append(n9)

print(p)

player1(list1,a)

print("It's a Tie!!")

print("Game Over\nThank you for playing")