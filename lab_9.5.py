name=input("please enter your name ")
print("hello, ", name)
price=float(input(" Please enter a price"))
discount=float(input(" Please enter the percent off "))
total_price_after_discount=price-(price*(discount/100))
discount_price=price*(discount/100)
print(" The price afetr the sale is $",total_price_after_discount)
print(" You saved $",discount_price," On your order ")

