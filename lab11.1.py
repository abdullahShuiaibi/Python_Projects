'''
Programmer: Abdullah Shuiaibi
Program name: GrossPay
Purpose: Compute Gross Income
'''
#Global Constants
REGULAR_HOURS = 40
OT_FACTOR = 1.5

def main():
    hours = float(input("Enter number of hours worked: "))
    rate  = float(input("Enter reqular pay rate: "))
    payCal(hours,rate) 

def payCal(arg1,arg2):
    if arg1 >  REGULAR_HOURS:
        otPay(arg1,arg2)
    else:
        rgPay(arg1,arg2)

def otPay(arg1,arg2):
    ot_Hours = arg1 - REGULAR_HOURS         # calc over time hours worked
    reg_Pay = (arg1 - ot_Hours) * arg2      # reg amount of money earned up to 40 hours
    ot_Pay = ot_Hours * (arg2 * OT_FACTOR ) # how much more money is earned for over time (> 40 hours ) money earned
    grossPay = reg_Pay + ot_Pay             # money made for 40 hrs + money made for over time
    print("You have worked " , arg1 , " hrs and your grossPay is $" , format(grossPay,",.2f"),sep='')

def rgPay(arg1,arg2):
    grossIncome = arg1 * arg2               # amount of money earned without over time
    print("You have worked " , arg1 , " hrs and your gross pay is $" , format(grossIncome,",.2f"),sep='')

main()
