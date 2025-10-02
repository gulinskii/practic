x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

a = (x1 + y1) % 2
b = (x2 + y2) % 2

if a == b:
    print("Yes")
    if a or b > 0:
        print("Black")
    else:
        print("White")
else: 
    print("No")