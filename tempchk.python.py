def main():
    count = 0
    while count == 0:
        temp = float(input("Enter the substance's Celsius temperature: "))
        if temp > 102.5:
            print("The temperature is too high.\nTurn the thermostat down and wait\n5 minutes.Then take the temperature\nagain and enter it.")
        else:
            count+=1

    print("The temperature is acceptable.\nCheck it again in 15 minutes.")
        
main()