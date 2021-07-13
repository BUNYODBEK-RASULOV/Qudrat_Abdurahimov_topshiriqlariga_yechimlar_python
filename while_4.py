# 4-topshiriq
n = float(input("N sonini kiriting:"))
i=0
while(n/3>=1):
    i=i+1
    n=n/3
else:
    if(n==1):
        print("kiritilgan son 3 ning {}-darajasi".format(i))
    else:
        print("3 ning darajasi emas")