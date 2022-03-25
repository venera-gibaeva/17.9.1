enter_list = input("Введите список чисел,разделенных пробелом:").split()
num_list = list(map(int, enter_list ))
element = int(input("Введите любое число :"))
num_list.append(element)
num_list = sorted(num_list)
left = 0
right = len(num_list) - 1

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print("Введенный список :", enter_list)
print("Список чисел :", num_list)
print(f'Before sorting: {num_list}')
print(f'After sorting: {num_list}')
print(binary_search(num_list, element, left, right))








