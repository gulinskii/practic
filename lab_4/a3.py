packets = input()

max_len = 0
now_len = 0

#длинная оследовательность потерянных пакетов
for j in packets:
    if j == '0':
        now_len +=1
        max_len = max(max_len, now_len)
    else:
        now_len = 0

#процент потерь
perecent = 100 * packets.count('0') / (packets.count('1') + packets.count('0'))

#проверка качества связи
if perecent <= 1:
    quality = "Отличное качество"
elif perecent > 1 and perecent <=5:
    quality = "Хорошее качество"
elif perecent >5  and perecent <= 10:
    quality = "Удовлетворительное качество"
elif perecent > 10 and perecent <= 20:
    quality = "Плохое качество"
else:
    quality = "Критическое состояние сети"

if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:
    print("Общее количество пакетов: {0}"
          "\nКоличество потерянных пакетов: {1}"
          "\nДлина самой длинной последовательности потерянных пакетов: {2}"
          "\nПроцент потерь: {3:.1f}%"
          "\nКачество связи: {4}".format(packets.count('1') + packets.count('0') , packets.count('0'), max_len, perecent, quality))

