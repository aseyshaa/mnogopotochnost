import threading

# Функция, которую будут выполнять потоки
def calculate_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Сумма чисел: ", sum)

# Создание списка чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Разделение списка на две части
mid = len(numbers) // 2
first_half = numbers[:mid]
second_half = numbers[mid:]

# Создание потоков
thread1 = threading.Thread(target=calculate_sum, args=(first_half,))
thread2 = threading.Thread(target=calculate_sum, args=(second_half,))

# Запуск потоков
thread1.start()
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()

print("Программа завершена.")

