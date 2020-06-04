def main():
    days = int(input("Enter number of days: "))
    pen=0.01
    for i in range(1,days+1):
        print(i,"\t$",format(pen,",.2f"), sep="")
        pen = (pen * 2)

       
	



main()
