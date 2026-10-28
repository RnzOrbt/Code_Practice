import random
import string as str



def randomizer(User):
    print("Your Letter is:", User)
    guess=random.choice(str.ascii_letters)
    print("The letter is...!", guess)
    try:
        if User==guess:
            try:
                hatdog=print(input("You Won! Try Again? True/False: "))
                if hatdog==True:
                    wait()
                elif hatdog==False:
                    print("Thanks For Playing!")
            except ValueError:
                    print("Value Not recognize. Please put only True/False!")

        elif User!=guess:
            try:
                buns=print(input("You Lost! Try Again? True/False"))
                if buns==True:
                    wait()

                elif buns==False:
                    print("Thanks For Playing!")
            except ValueError:
                    print("Value Not recognize. Please put only True/False!")
    except Exception:
            print("Error please Run it Again!")


def wait():   
    while True:
        User=input("Enter a Letter: " )
        try:
            if User=="":
                print("Write Something")
                continue
            elif len(User)==1 and User.isalpha():
                randomizer(User)
            elif len(User)!=1:
                print("Write only 1 letter!")
                continue
            elif User.isdigit():
                print("Letters Only bro")
                continue

        except Exception:
            print("Follow Instructions!!!")
            break
wait()

