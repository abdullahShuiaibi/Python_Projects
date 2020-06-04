'''
Programmer: Abdullah Shuiaibi
Program name: TaxCalculator
Purpose: Compute personal Income Tax
'''
#Global Constants
TAX_RATE = 20/100
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000

#Input Request

def main():
    gross_Income = float(input("Enter gross Income: "))
    dependents = int(input("Enter the number of dependents: "))
    taxCal(gross_Income,dependents)

#Tax Calculator
def taxCal(arg1,arg2):
    taxable_Income = (arg1-STANDARD_DEDUCTION-(DEPENDENT_DEDUCTION*arg2))*TAX_RATE
    print("The income tax is $ " , format(taxable_Income , "7,.2f"))

#Main function call
main()
