import random
def main():
    # Code here
    print("Hello Player!")
    nameString = input("What is your name? ")
    answ=input("What operation do you want to use? ")
    num1=input("Enter a number ")
    num2=input("Enter a second number ")
    if answ == "Addition":
        print(str(int(num1)+int(num2)))
    elif answ == "Subtraction":
        print(str(int(num1)-(num2)))
    elif answ == "Multiplication":
        print(str(int(num1)*int(num2)))
    elif answ == "Division":
        print(str(int(num1)/int(num2)))
    else:
        print("That is not an operation!")
    number1 = input("Enter a number ")
    sol=int(number1)*2
    print("The number you entered when multiplied by 2 is now "+ str(sol))
    number2 = input("Now enter an even number ")
    sol2=int(number2)/2
    print("Your number divided by 2 is now "+ str(sol2))
    print("Bye!!!")
    return 0
    
    
if __name__ == "__main__":
    main()