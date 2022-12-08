array = list(map(int, input('введите числа через пробел: ').split())) # вводим числа в массив

print(array) # выводим их на экран

element = int(input('Введите число в рамках последовательности: ')) # вводим число, которое хотим добавить в массив
while element:
    if element not in range(min(array) + 1, max(array)): # если введенное число вне рамок последовательности
        print('Некорректное число')
        element = int(input('введите число в рамках последовательности: ')) # повторяем, пока число не будет в рамках последовательности
    else:
        break

array.append(element)
# используем метод сортировки выбором
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(array)


def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
    middle = (right + left) // 2 # находим середину
    if array[middle] == element: # если элемент в середине
        return middle - 1 # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        return binary_search(array, element, left, middle - 1) # рекурсивно ищем в левой половине
    else: # иначе в правой
        return binary_search(array, element, middle + 1, right)


a = (binary_search(array, element, 0, len(array) - 1))
print(a)