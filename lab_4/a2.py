n = int(input())
m = int(input())

print("ПРЯМОУГОЛЬНИК {0}*{1}:".format(n, m))
for i in range(n):
   for j in range(m):
        print("#", end="")
   print()

print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(n):
    for i in range(i + 1):
        print("#", end="")
    print()

print("\nРАМКА {0}*{1}:".format(n, m))
for i in range(n):
    if i == 0 or i == n - 1:
        print("#" * m)
    else:
        print("#" + " " * (m - 2) + "#")
