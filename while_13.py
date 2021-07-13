# 13-topshiriq
n = int(input("N sonini 1<N~16 kiriting:"))
# N ga 16 dan katta qiymat bersangiz hisoblashga ko'p vat ketadi.
k = 0
s = 0
while (s <= n):
    k = k + 1
    s = s + 1 / k
print("k=", k - 1)
print("yig'indi s=", s - 1 / k)
