# 5-topshiriq
n = float(input("N sonini kiriting:"))
i=0
while(n/2>=1):
    i=i+1
    n=n/2
else:
    if(n==1):
        print("kiritilgan son 2 ning {}-darajasi".format(i))
    else:
        print("2 ning darajasi emas")