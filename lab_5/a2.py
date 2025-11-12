import re

text = input()

sentences = re.split(r'(?<=[.?!]) ', text)
total = 0
for i in sentences:
    total += 1
    print(i)
print(f"Предложений в тексте: {total}")
