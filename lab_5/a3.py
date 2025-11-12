text = input()

num = text.split()

result = ""
for n in num:
    if n[0].isupper() and len(n) >= 3:
        result += n[0]

print(result)