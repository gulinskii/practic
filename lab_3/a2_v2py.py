#второй вариант

import string 

password = input("Введите пароль: ")


allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'

# Список для хранения ошибок
errors = []

if len(password) != 8:
    errors.append("Длина пароля не равна 8")

if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")

if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")

if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")

if not any(symbol in "*-#" for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")

if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")

if not errors:
    print("Надежный пароль")
else:
    for err in errors:
        print(err)