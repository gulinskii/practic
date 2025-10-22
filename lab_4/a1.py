import random 
import time 

own_time = time.time()

N  = int(input("Введите количество примеров: "))

currect_result = 0

for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    while True:
        try:
            start_time = time.time()
            answer = int(input("{0} * {1} = ".format(a, b)))
            spend_time = time.time() - start_time
            if a * b == answer:
                print("Верно!(Время: {0:.2f} сек)".format(spend_time))

            else:
                print("Неверно! Правильно: {0} (Время: {1:.2f})".format(a*b, spend_time))
            break
        except ValueError: 
            print("Пожалуйста, введите целое число!")

    if a * b == answer:
        currect_result += 1

end_time = time.time() - own_time
percentage =  currect_result / N * 100

print("==================================================\nСТАТИСТИКА\n==================================================")
print("Общее время: {0:.1f} \nСреднее время на вопрос: {1:.2f} \nПравильных ответов: {2}/{3}\nПроцент правильных: {4:.0f}".format(end_time,end_time / N,  currect_result, N, percentage))