banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
job=open("str.txt","w")
for i in banks_list:
    # job=open("str.txt","w")
    value=job.write(i)
    print(i)

job.close()