def main():
    price = float(input("Enter the sales amount: "))
    county_tax = float(input("Enter county tax percentage: "))/100
    state_tax = float(input("Enter state tax percentage: "))/100
    totalTax(price,county_tax,state_tax)
    
    
def totalTax(price,county_tax,state_tax):
    county_tax = price * county_tax
    state_tax = price * state_tax
    total_tax = county_tax+state_tax
    total_sale = price-total_tax
    print("The amount of county tax is: $" , format(county_tax,"7,.2f"))
    print("The amount of state tax is: $" , format(state_tax,"7,.2f"))
    print("The total sale is: $" , format(total_sale,"7,.2f"))#Total sale after tax
    print("The total tax amount: $" , format(total_tax,"7,.2f"))



main()
