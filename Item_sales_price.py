DISCOUNT = 25/100
def main():
    price = get_regular_price()
    discount = cal_discount(price)
    total = sale_price(price,discount)
    print("The sale price of the item is $",format(total,".2f"),sep="")
def get_regular_price ():
    price = float(input("Enter the item's reqular price: "))
    return price
def sale_price(price,discount):
    total = price - discount
    return total
def cal_discount(price):
    total = price*DISCOUNT
    return total

main()