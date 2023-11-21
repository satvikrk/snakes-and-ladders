import random
pos=1
score=0

ladders = {2: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}
snakes = {32: 10, 34: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}


def diceroll():
    opt=input("Do you wish to roll the dice? (y/n): ")
    if opt=="y":
        return True
    else:
        return False

def board(pos):
    print(" ----------------------------------------------------------- ")
    for i in range (10, 0, -1):
        print("|" , end="")
        for j in range(10*i, (10*i) - 10, -1):
            if j==pos:
                print("  ", "•", end=" |")
            elif j==100:
                print("", j, end=" |")
            elif j>9 and j<100:                print(" ", j, end=" |")
            elif j>0 and j<10:
                print("  ", j, end=" |")
        print("")
    print(" ----------------------------------------------------------- ")

board(pos)

while pos<100:
    if diceroll():
        pos+=random.randint(1,6)
        print("\nYour position is", pos)
        if pos in snakes:
            print("You have been bitten by a snake!")
            pos=snakes[pos]
            print("\nYour position is", pos)
        elif pos in ladders:
            print("You have climbed up a ladder!")
            pos=ladders[pos]
            print("\nYour position is", pos)
        board(pos)

if pos>=100:
    print("You win!")