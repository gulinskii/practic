wased = int(input("Введите показания с счетчика за прошлый месяц: "))
new = int(input("Введите показания счетчика за текущий месяц: "))

if wased < new:
    result = new - wased
elif wased > new:
    result = 9999 - wased + 1 + new

if result <= 300:
    price = 21
    print("Предыдущее: {0}\nТекущее: {1}\nИспользовано: {2}\nК оплате: {3}\nФиксированная сумма: {4}"
    .format(wased, new, result, price, price))

elif result > 300 and result <= 600:
    price = 21 + (result - 300) * 0.06
    price_double = price / result

    print("Предыдущее: {0}\nТекущее: {1}\nИспользовано: {2}\nК оплате: {3}\nСр. цена m^3: {4:.2f}"
    .format(wased, new, result, price, price_double))

elif result > 600 and result <= 800:
    x = result - 300
    y = x - 300

    price = 21 + (y * 0.04) + (300 * 0.06)
    price_double = price / result
    
    print("Предыдущее: {0}\nТекущее: {1}\nИспользовано: {2}\nК оплате: {3}\nСр. цена m^3: {4:.2f}"
    .format(wased, new, result, price, price_double))

else:
    price = 21 + (300 * 0.06) + (200 * 0.04) + (result - 300 - 200 - 300) * 0.025
    price_double = price / result
    
    print("Предыдущее: {0}\nТекущее: {1}\nИспользовано: {2}\nК оплате: {3}\nСр. цена m^3: {4:.2f}"
    .format(wased, new, result, price, price_double))
