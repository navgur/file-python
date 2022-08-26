chr=open("str.txt","w")
name=[]
for i in range(5):
    val=str(input("enter the number="))
    name.append(val)
chr.writelines(name)
print(name)
chr.close()


# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# job=open("str.txt","w")
# for i in banks_list:
#     # job=open("str.txt","w")
#     value=job.write(i)
#     print(i)

# job.close()