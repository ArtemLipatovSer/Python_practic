import random


# # Пузырьковая сортировка
# def bubble_sort(arr, check):
#     n = len(arr)
#     if not check:
#         for i in range(n):
#             for j in range(0, n-i-1):
#                     if arr[j] < arr[j+1]:
#                         arr[j], arr[j+1] = arr[j+1], arr[j]
#     else:
#         for i in range(n):
#             for j in range(0, n-i-1):
#                     if arr[j] > arr[j+1]:
#                         arr[j], arr[j+1] = arr[j+1], arr[j]
# #     pass
# # # Пасс значит функция ничего не делает


# Сортировка втсавкой
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     left = [x for x in arr if x < pivot]
#     equal = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     sorted_left = quick_sort(left)
#     sorted_right = quick_sort(right)
#
#     result = sorted_left + equal + sorted_right
#     return result

# # Линейный поиск
# def line_search(arr, el):
#     for index, item in enumerate(arr):
#         if item == el:
#             return index
#         if index == len(arr)-1 and item != el:
#             return -1

# Бинарный поиск

def binary_search(arr, target):
    low, height = 0, len(arr)-1

    while low <= height:
        midl = (low + height) // 2
        midl_value = arr[midl]

        if midl_value == target:
            return midl
        elif midl_value < target:
            low = midl + 1
        elif midl_value > target:
            height = midl - 1
    return -1

if __name__ == '__main__':
    my_array = [random.randint(0,100) for i in range(10)]
    # print(my_array)
    # bubble_sort(my_array, 1)
    insert_sort(my_array)
    print(my_array)
    # print(quick_sort(my_array))
    # print(line_search(my_array, 10))
    print(binary_search(my_array, 1))
