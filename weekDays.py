def main():
    weekDays_file = open("weekDays.txt","w")


    daysList = ["Monday\n","Tuesday\n","Wendsay\n","Thursday\n",
                "Friday\n","Saturday\n","Sunday\n"]

    for i in daysList:
        weekDays_file.write(i)
    weekDays_file.close()
    weekDays_file = open("weekDays.txt","r")  
    print(weekDays_file.read())
    weekDays_file.close()

main()
