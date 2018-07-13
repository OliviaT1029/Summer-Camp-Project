import random
def main():
    # Code here
    print("Hello Player!")
    nameString = input("What is your name? ")
    print("Hello " + (nameString))
    randomnum=random.randint(1,2)
    answ=input("What is the random number? ")
    if answ == randomnum:
        print("You are correct!")
    print("Bye!")
    return 0
    
main()