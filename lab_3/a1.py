x1 = int(input("Введите координаты x1: "))
y1 = int(input("Введите координаты y1: "))
x2 = int(input("Введите координаты x2: "))
y2 = int(input("Введите координаты y1: "))


if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0:
    print("Все координаты не должны быть равными нулю.")
if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
    print("Yes, I")
elif x1 < 0 and x2 < 0 and y1 < 0 and y2 <0:
    print("Yes, III")
elif x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0:
    print("Yes, IV")
elif x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0:
    print("Yes, II")
else:
    print("No")


