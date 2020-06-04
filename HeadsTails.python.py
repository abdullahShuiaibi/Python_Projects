import random

HEADS = 1
TAILS = 2
TOSSES = 10
def main():
    for i in range(TOSSES):
        x = random.randint(HEADS,TAILS)
        if x == HEADS:
            print("Heads")
        else:
            print("Tails")
main()