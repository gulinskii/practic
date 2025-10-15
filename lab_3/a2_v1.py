#первый вариант 

import string

password = input("Введите пароль: ")

char_len = False
for char in password:
    if len (password) == 8:
        char_len = True
        break
if not char_len:
    print("Длина пароля не равна 8")

for char in password:
    if password == password.lower():
        print("Отсутствуют заглавные буквы")
        char_lower = False
        break
    else: 
        char_lower = True
        break

for char in password:
    if password == password.upper():
        print("Отсутствуют строчные буквы")
        char_upper = False
        break
    else:
        char_upper = True
        break

char_number = False
for char in password:
    if any(symbol.isdigit() for symbol in password) == True:
        char_number = True
        break
if not char_number:
    print("В пароле отсутствуют цифры")

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
char_allowed = False
for char in password:
    if all(symbol in allowed for symbol in password) == True:
        char_allowed = True
        break
if not char_allowed:
    print("В пароле используются непредусмотренные символы")

char_symbol = "*-#"
char_text = False

for char in password:
    if any(char in password for char in char_symbol):
        char_text = True
        break
if not char_text:
    print("В пароле отсутствуют специальные символы")

if char_len == True and char_lower == True and char_upper == True and char_number == True and char_text == True and char_allowed == True:
    print("Пароль надежный!")