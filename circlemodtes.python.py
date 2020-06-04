import circlemod
def main():
   
    def menu():
        num=0
        while num !=5:
            print("menu")
            print("1) Area of circle")
            print("2) circum of circle")
            print("3) Area of rectangle")
            print("4) circumfernce of circle")
            print("5) End")
            num = int(input())
            if num ==1:
                output=circlemod.area_circle(float(input("enter radius: ")))
                
            elif num ==2:
                circlemod.cir_circle(float(input("enter radius: ")))
                
            elif num== 3:
                w=int(input("Enter width: "))
                l=int(input("enter lenght: "))
                output=circlemod.area_rec(w,l)
               
            elif num==4:
                w=int(input("Enter width: "))
                l=int(input("enter lenght: "))
                output=circlemod.cir_rec(w,l)
                
        print("You have ended the menu ")
    menu()
main()
