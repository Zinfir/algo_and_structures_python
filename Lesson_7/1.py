"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint

def bubble_sort(array):
    """ Bubble sort function """
    n = 1
    while n < len(array):
        changed = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changed = True
        n += 1
        if not changed:
            break

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 

if __name__ == '__main__': 
    array = [randint(-100, 100) for _ in range(10)]
    printList(array)
    bubble_sort(array)
    printList(array)
