def main():
    intro()
    Fahrenheit=float(input(" Enter the temperture in Fahrenheit "))
    Convert(Fahrenheit)



def intro():
    name=input(" Enter your name ")
    print(f" Hello {name}\n This program converts Fahrenheit to celsius ")
    




def Convert(Fahrenheit):
    
    celsius=(Fahrenheit-32)*(5/9)
    print(f"Fahrenheit|celsius")
    print(Fahrenheit,"|",format(celsius,".2f") ,"C")




main()
     
