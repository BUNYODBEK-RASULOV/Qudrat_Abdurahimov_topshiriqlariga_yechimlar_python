# 16-topshiriq
p = float(input("yuguruvchining foizi 0<p<50% ni  kiriting:"))
s = 10  # boshlangich masofa
a = 200  # marra
ss = 10  # 1-kuni yugurgani uchun
i = 1  # kunlar soni
while (ss <= a):
    s = s * (1 + p / 100)
    # s bu i- kuni yugurgan masofasi
    ss = ss + s
    # ss jami qancha yugurgani
    i = i + 1
    print("Sportsmen {}-kun jami {} km masofani bosib utadi;".format(i, ss))
