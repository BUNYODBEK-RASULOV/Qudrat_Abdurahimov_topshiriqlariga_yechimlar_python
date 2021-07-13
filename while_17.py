# 17-topshiriq
n = int(input("N sonini N>M>0 kiriting:"))
m = int(input("M sonini M>0 kiriting:"))
i = 0  # butun qism
while (n - m >= 0):
    n = n - m
    i = i + 1
print("burun qismi:", i)
print("qoldiq:", n)
