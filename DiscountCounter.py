'''
Programmer: Abdullah Shuiaibi
Program name: DiscountCounter
Purpose: Count the discount based on quantity
'''
# Global Varible
RETAIL_PRICE = 99
def main():
    quantity = float ( input ("Enter the quantity of the item: "))
    calDisc(quantity)
def calDisc(arg1):
    price = arg1 * RETAIL_PRICE
    if arg1 >= 10 and arg1 <= 19:
        discount = 20/100
        Total = price - (price * discount)
        print ("The total price is $", format(Total,",.2f"))
        print("You recived a %", (discount*100)," discount")
        print("You saved $", discount * price)
    elif  arg1 >= 20 and arg1 <= 49:
            discount = 30/100
            Total = price - (price * discount)
            print ("The total price is $", format(Total,",.2f"))
            print("You recived a %", (discount*100)," discount")
            print("You saved $", discount * price)
    elif arg1 >= 50 and arg1 <= 99:
            discount = 40/100
            Total = price - (price * discount)
            print ("The total price is $", format(Total,",.2f"))
            print("You recived a %", (discount*100)," discount")
            print("You saved $", discount * price)
    elif arg1 > 99 :
            discount = 50/100
            Total = price - (price * discount)
            print ("The total price is $", format(Total,",.2f"))
            print("You recived a %",(discount*100)," discount")
            print("You saved $",discount * price)
    elif arg1 < 10: 
         discount = 0/100
         Total = price - (price * discount)
         print ("The total price is $", format(Total,",.2f"))
         print("Your quantity is to low for a discount")       
    else:
         print("Invalid Input")
main()
