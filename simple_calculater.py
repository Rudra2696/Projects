def add(a,b):
    return a+b

def sub(a,b):
    return a-b  

def mul(a,b):
    return a*b  

def mod(a,b):
    return a%b


def div(a,b):
    return a/b

while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))
        break
    else:
        print("Please choose 1/2/3/4/5 only") 