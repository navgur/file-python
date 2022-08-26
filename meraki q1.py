obj1=open("city.txt","w")
for i in range(3):
    name=str(input("enter the name="))
    obj1.write(name)
    obj1.write ('\n')
obj1.close() 