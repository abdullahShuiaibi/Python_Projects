DOLLOR = 100

def main():
    pen = int(input("Enter number of pennies: "))*1
    nickles = int(input("Enter number of nickles: "))*5
    dimes = int(input("Enter number of dimes: "))*10
    querters = int(input("Enter number of quaters: "))*25
    dolAmount(pen,nickles,dimes,querters)

def dolAmount(arg1,arg2,arg3,arg4):
    total = arg1+arg2+arg3+arg4
    ckAmount(total)

def ckAmount(total):
    if total == DOLLOR:
        print("Amount entered is $1 dollor")
    elif total > DOLLOR:
        print("Amount entered is more a dollor")
    elif total < DOLLOR:
        print("Amount entered is less than a dollor")
    
main()
    
    
