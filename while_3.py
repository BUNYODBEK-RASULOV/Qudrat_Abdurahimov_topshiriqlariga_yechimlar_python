# 3-topshiriq
n = float(input("N sonini kiriting:"))
k = float(input("K sonini kiriting:"))
nn=n
# nn dan javobni chiqarguncha foydalanamiz shunda n ning asl qiymatini saqlab quyamiz
i=0
while(n-k>0):
    i=i+1
    n=n-k
else:
    print("{} ni {} ga bo'lgandagi qoldiq {} butun qism esa {}".format(nn,k,n,i))