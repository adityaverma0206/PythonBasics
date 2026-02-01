n1 = float(input("enter no 1="))
n2 = float (input("enter no 2="))
choice = input("enter your choice = + / // * ** - ")
if choice == "+":
    print(f"add:{n1+n2}")
elif choice == "-":
    print(f'sub:{n1-n2}')
elif choice == "*":
    print(f'mul:{n1*n2}')
elif choice == "/":
    print(f'div:{n1/n2}')
elif choice == "//":
    print(f"floatdiv:{n1//n2}")
elif choice == "**":
    print(f"exp:{n1**n2}")
else :
    print("invalid") 
