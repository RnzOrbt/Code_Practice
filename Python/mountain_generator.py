def char(height, design):
    for a in range(1, height + 1):
        space = " " * (height - a)
        strdesign = ("" + design + " ") *(a)
        print(space + strdesign)


def loops():
    while True:
        height = input("How tall is your Mountain?: ")
        if height.isdigit():
            height = int(height)
            break
        else:

            print("Whole Number Only!")
            continue

    while True:  
        design = input("Select a Single Character Design: ")
        if len(design) == 1:
            char(height, design)
            break

        else:
            print("Single Character Only!.")
            continue

def restart():
    while True:
        loops()
        restart= input("Do you wish to continue?True/False")
        if restart=="True":
            continue

        else:
            print("Thanks for using this bro!")
            break
restart()