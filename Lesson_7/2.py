"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import timeit
import random




def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
          

        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  

def printList(arr): 
    for i in range(len(arr)):         
        print(format(arr[i], '.2f'),end=" ") 
    print() 
  

if __name__ == '__main__': 
    arr = [50 * random.random() for _ in range(10)]  
    print("Исходный массив: ")  
    printList(arr) 
    mergeSort(arr) 
    print("Отсортированный массив: ") 
    printList(arr)
    print('Время выполнения: ', timeit.timeit("mergeSort(arr)", \
    setup="from __main__ import mergeSort, arr", number=10))
