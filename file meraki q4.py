city=open("city.txt","r")
for i in city:
    if "delhi" in i:
        city=open("delhi.txt","a") 
        city.write(i)
    elif "shimla" in i:
        city=open("shimla.txt","a")
        city.write(i)
    else:
        city =open("other.txt","a")       
        city.write(i)