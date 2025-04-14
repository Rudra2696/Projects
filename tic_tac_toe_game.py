print("Welcome to tic tac toe game")

print(f"For O Enter 1\n For X Enter 2")

print("""

1 | 2 | 3
----------      
4 | 5 | 6
----------      
7 | 8 | 9


""")

while True:
    try:
        n=int(input("What is your choice : "))
        if (n==1 or n==2):
            break
        else:
            print("Enter 1/2 only")
    except(ValueError,SyntaxError,TypeError):
        print("Invalid Input")
        
                