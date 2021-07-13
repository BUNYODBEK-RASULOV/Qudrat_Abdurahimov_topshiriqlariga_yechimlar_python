# 15-topshiriq
s = int(input("S sonini  kiriting:"))
p = float(input("Bank foizi ni (%) kiriting:"))
a = 2 * s
i = 0
while (s < a):
    s = s * (1 + p / 100)
    i = i + 1
print(i, " oydan so'ng sizning pulingiz s=", s, " so'm bo'ladi.")
