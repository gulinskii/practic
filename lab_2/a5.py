a = int (input("Ведите первое число: "))
b = int(input("Ведите второе число: "))

result = ["NO", "YES"][a % b == 0]
print(result)    