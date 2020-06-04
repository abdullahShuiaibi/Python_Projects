
className = open("nameList.txt","w")
classList=["mark","arnold","alex"]
i=0
while i <= 2:

    className.write(classList[i])
    i+=1

className.close()
