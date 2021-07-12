# 1-usul
# b=int(input("sonni kiriting:"))
# a=int(input("takrorlanishlar sonini kiriting:"))
# # for x in range(a):
# #     print(b)

# 2-usul
# i=0
# while i<a:
#     print(b)
#     i=i+1

# 2-misol
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonni kiriting:"))
# n=0
# for x in range(a,b+1):
#     n=n+1
#     print(x)
# print(n," ta son bor ")


# 3-misol
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonni kiriting:"))
# n=0
# for x in range(a,b):
#     n=n+1
#     print(b-x+a)
# print(n," ta son bor ")

# 7-misol
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonni kiriting:"))
# s=0
# for x in range(a,b):
#     s=s+x
# print(s)

# 8-misol
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonni kiriting:"))
# s=1
# for x in range(a,b):
#     s=s*x
# print(s)

# 9-misol
# kvadralarining yig'indisini hisoblaydi
# a=int(input("a sonini kiriting:"))
# b=int(input("b sonni kiriting:"))
# s=0
# for x in range(a,b):
#     s=s+x**2
# print(s)


# 10-misol
# n=int(input("n sonini kiriting:"))
# s=0
# for x in range(1,n+1):
#     s=s+1/x
# print(s)
# print(len(range(1,n+1)))

# 11-misol
# n=int(input("n sonini kiriting:"))
# s=0
# for x in range(n+1):
#     s=s+pow(n+x,2)
# print(s)

# 12-misol
# n=int(input("n sonini kiriting:"))
# s=1
# for x in range(n+1):
#     s=s*(1+x/10)
# print(s)

# 13-misol
# n=int(input("n sonini kiriting:"))
# s=0
# for x in range(n+1):
#     s=s+(1+x/10)*pow(-1,x)
# print(s)

# 14-misol
# n=int(input("n sonini kiriting:"))
# s=0
# for x in range(1,n+1):
#     s=s+2*x-1
#     print(s)
# print(s)

# 15misol
# a=float(input("a sonini kiriting:"))
# n=int(input("n sonini kiriting:"))
# s=1
# for x in range(1,n+1):
#    s=s*a
# print(s)

# 16-misol
# a=float(input("a sonini kiriting:"))
# n=int(input("n sonini kiriting:"))
# s=1
# for x in range(1,n+1):
#    s=s*a
#    print(s)

# 17-misol
# a=float(input("a sonini kiriting:"))
# n=int(input("n sonini kiriting:"))
# s=1
# aa=1
# for x in range(n+1):
#     aa=aa*a
#     s=s+aa
#     print(s)

# 18-misol
# a=float(input("a sonini kiriting:"))
# n=int(input("n sonini kiriting:"))
# s=1
# aa=1
# for x in range(n+1):
#     aa=aa*a
#     s=s+aa*pow(-1,x+1)
#     print(s)

# 19-misol
# n=int(input("n sonini kiriting:"))
# s=1
# for x in range(1,n+1):
#     s=s*x
# print(s)

# 21-misol
# n=int(input("n sonini kiriting:"))
# s=1
# ss=1
# for x in range(1,n+1):
#     s=s*x
#     ss=ss+1/s
# print(ss)

# 22-misol bu dastur e^y ni hisoblab beradi n aniqliq darajasi.
# n=int(input("n aniqlikni kiriting:"))
# y=float(input("y ga qiymat bering"))
# #yy y ni darjasi
# yy=1
# #ii i! ni ifoda etadi
# ii=1
# ss=1
# for i in range(1,n+1):
#     yy=yy*y
#     ii=ii*i
#     ss=ss+yy/ii
# print(ss)


# 23-misol
# n=int(input("n aniqlikni kiriting:"))
# y=float(input("y ga qiymat bering"))
# ii = -1
# ss = 0
# for i in range(1,2*n+2):
#     ii = ii * i
#     if(i%2==1):
#         yn=pow(y,i)
#         ss=ss-yn/ii
#         ii=-ii
# print(ss)

# 24-misol
# n=int(input("n aniqlikni kiriting:"))
# y=float(input("y ga qiymat bering:"))
# ii = -1
# ss = 1
# for i in range(2,2*n+2):
#     ii = ii * i
#     if(i%2==0):
#         yn=pow(y,i)
#         ss=ss+yn/ii
#         ii=-ii
# print(ss)

# 25-misol
# n=int(input("n aniqlikni kiriting:"))
# y=float(input("y ga qiymat bering"))
# ss = 0
# for i in range(1,2*n+2):
#     yn=pow(y,i)
#     ss=ss+(pow(-1,i-1))*yn/i
# print(ss)

# 26-misol
# n=int(input("n aniqlikni kiriting:"))
# y=float(input("y ga qiymat bering"))
# s=0
# for i in range(0,n):
#     #"har safar s ga yangi qiymatini qo'shib ketadi, pow esa darajai hisoblash uchun"
#     s=s+pow(-1,i)*pow(y,2*i+1)/(2*i+1)
# print("Yig'insi ning qiymati s=",s)

# 27-misol
# n = int(input("n butun sonni kiriting: "))
# x = float(input("x haqiqiy sonni |x|<1 kiriting:"))
# s = x
# tf = 1  # tf toq faktoriallar
# jf = 1  # jf juft faktoriallar
# for i in range(1, n):
#     tf = tf * (2 * i - 1)
#     jf = jf * (2 * i)
#     s = s + pow(x, 2 * i + 1) * tf / (jf * (2 * i + 1))
# print("Berilgan ifadaning yig'indisi s=", s)
# ko'rsatma har safar kasirning maxrajida  oxirgi son toq ekanligiga etibor bering

# 28-misol
# n = int(input("n sonni kiriting n>0 bo'lsin:"))
# x = float(input("x sonni kiriting |x|<1 bo'lsin:"))
# s = 1 + x / 2  # ifodaning boshlang'ich qiymati
# jf = 2
# tf = 1
# for i in range(2, n):  # sanash 2 dan boslanadi
#     tf = tf * (2 * i - 3)
#     jf = jf * (2 * i)
#     s = s + pow(-1, i - 1) * pow(x, i) * tf / jf
# print("Ifodaning qiymati s=", s)

# 29-misol
# n = int(input("n butun sonni kiriting:"))
# a = float(input("[A,B] kesmaning boshi A kiriting:"))
# b = float(input("[A,B] kesmaning oxiri B kiriting:"))
# d = (b - a) / n
# for x in range(n):
#     a = a + d
#     print("{}-nuqtaning kordinatasi {} ".format(x + 1, a))

# 30-misol
# import math
#
# n = int(input("n butun sonni kiriting:"))
# a = float(input("[A,B] kesmaning boshi A kiriting:"))
# b = float(input("[A,B] kesmaning oxiri B kiriting:"))
# d = (b - a) / n
# for x in range(n):
#     a = a + d
#     F = 1 - math.sin(a)
#     print("{}-nuqta kordinatasi:{} F({}) = {}".format(x + 1, a, a, F))

# 31-misol
# n = int(input(" qadamlar soni n>0 sonni kiriting:"))
# a = 2
# for i in range(n):
#     a = 2 + 1 / a
#     print("{} qadamda {}".format(i, a))

# 32-misol
# n = int(input(" qadamlar soni n>0 sonni kiriting:"))
# a = 2
# for i in range(n):
#     a=(a+1)/n
#     print("A({})={}".format(i,a))

# 33-misol
# n = int(input(" qadamlar soni n>1 sonni kiriting:"))
# f=1
# x=1
# for i in range(3,n+1):
#     f=x+f
#     x=f-x
#     print("F({})={}".format(i,f))

# 34-misol
# n = int(input(" qadamlar soni n>3 sonni kiriting:"))
# f=2
# x=5.0/3
# for i in range(4,n+1):
#     y=f
#     f=(f+2*x)/3
#     x=y
#     print("A({})={}".format(i,f))

# 35-misol
# n = int(input("n in sonni kiriting:"))
# A = 1
# A2 = 2
# f = 3  # A3 deb f  olindi
# for i in range(4, n + 1):
#     aa = A2  # A2 ni dastlabki qiymatini saqlab quyamiz bo'lmasa o'zgarin ketadi.
#     aaa = f  # A3 ni ham qiymatini saqlab quyamiz bundan kiyinroq foydalanamiz.
#     f = f + A2 - 2 * A
#     A2 = aaa
#     A = aa
#     print(f)

# ichma ich for orqali yechiladigan misollar
# 36-misol
# n=int(input("n ning qiymatini kiriting:"))
# k=int(input("k ning qiymatini kiriting:"))
# s=0
# for i in range(1,n+1):
#     daraja=1
#     for j in range(1,k+1):
#         daraja=daraja*i
#     s=s+daraja
# print(s)

# 37-misol
# n=int(input("n sonini kiriting:"))
# sum=0
# for i in range(1,n+1):
#     pow=1
#     for j in  range(1,i+1):
#         pow=pow*i
#     sum=sum+pow
# print(sum)

# 38-misol
# n=int(input("n sonini kiriting:"))
# sum=0
# for i in range(1,n+1):
#     pow=1
#     for j in range(1,n+2-i):
#         pow=pow*i
#     sum=sum+pow
# print(sum)

# 39-misol
# import  math
# a=int(input("A sonini kiriting:"))
# b=int(input("B sonini kiriting:"))
# for i in range(a+1,b):
#     for j in range(int(math.fabs(i))):
#         print(i)
# math.fabc bu nodul belgisi,int qilishimizga sabab modul ichidan haqiqiy son chiqadi range esa butun sonlarsa ishlaydi.

# 40-topshiriq
# a = int(input("A sonini kiriting:"))
# b = int(input("B sonini kiriting:"))
# for i in range(1, b - a + 1):
#     for j in range(1, i + 1):
#         print(a + i)

# Rasulov Bunyodbek ishlab chiqdi:
# Savolar yoki kachiliklari bo'lsa izohda qoldiring.
