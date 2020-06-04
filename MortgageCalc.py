#Hello
price=float(input(" What is the price of the home "))
intrest=float(input(" What is the intrest rate "))
years=float(input(" In years how long would you need to pay off the loan "))
n=years*12
r=intrest/100/12
p=price-(price*0.20)
m=(r/(1-(1+r)**(-n))) * p
print(" The monthly Mortgage payments is $",format(m,"7,.2f"))
print(" The principle is ",format(p,"7,.2f"))
print(" The total months for paymenst is ",n," Months")
print(" The intrest rate per month is ",format(r,".7f"))

