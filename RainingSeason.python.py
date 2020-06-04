MONTHS=12
def main():
    years = int(input("Enter number of years: "))
    total = 0
    avg =0

    for i in range(1,years+1):
        for j in range(1,MONTHS+1):
            print("Enter the amount of rain in inches for month #",j," in the year ",years)
            inch = float(input(""))
            total = total + inch

    avg = total/j
    print("The number of months is: ",j*years)
    print("The total amount of rain for ",years," years is ",total," Inches" )
    print("The average amount of inches for ", years," years is ", avg," Inches")
main()
