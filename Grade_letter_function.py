# Lab 13.3
# may 28 2020
# Abdullah Shuiaibi LCS
# Program name: Grade_letter_function
# Purpose: Write a program that asks the user to enter five test scores. The program should display a letter grade 
# for each score and the average test score. Write the following functions in the program:

def main():
    def calc_average(arg1,arg2,arg3,arg4,arg5):
        total = arg1+arg2+arg3+arg4+arg5
        averge = total/5
        return averge
    def determine_grade(arg1):
        if arg1 > 89:
            letter = "A"
        elif arg1 > 79:
            letter = "B"
        elif arg1 > 69:
            letter = "C"
        elif arg1 > 59:
            letter = "D"
        elif arg1 < 60:
            letter = "F"
        else:
            letter = "Invalid"
        return letter
    num = 1
    while num!=2:
        grade1=float(input("Enter grade 1: "))
        grade2=float(input("Enter grade 2: "))
        grade3=float(input("Enter grade 3: "))
        grade4=float(input("Enter grade 4: "))
        grade5=float(input("Enter grade 5: "))
        grade = calc_average(grade1,grade2,grade3,grade4,grade5)
        print(int(grade))
        print(determine_grade(grade))
        end = int(input("1)Do it again: \n2)End:\n "))
        if end == 2:
            num+=1
    print("GoodBye") 
main()


