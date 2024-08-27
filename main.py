# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создание пустых списков для простых и не простых чисел
primes = []
not_primes = []

# Перебор всех чисел в списке numbers
for number in numbers:
    if number == 1:
        # Исключения числа 1, переход на следующий шаг цикла
        continue

    # Присвоение переменной is_prime значения True
    is_prime = True

    # Проверка делимости числа от 2 до корня квадратного из числа + 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            # Если найден делитель, число не простое
            is_prime = False
            break

    # Запись числа в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Вывод результатов
print("Primes:", primes)
print("Not Primes:", not_primes)
