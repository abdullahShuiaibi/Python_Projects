def main():
    speed = int(input("Enter a starting speed: "))
    i = int(input("Enter the incremental speed increase: "))
    calKPH(speed,i)
def calKPH(arg1,arg2):
    print("KPH     MPH")
    print("____________")
    for i in range(arg1,140,arg2):
        MPH=i*0.6214
        print(i,"\t",int(MPH))
main()
