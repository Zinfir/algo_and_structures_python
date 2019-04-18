"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random

m = 5
arr = [random.randint(0, 100) for _ in range(2*m + 1)]

print("array = ", arr)

def mysort(arr, index):
        """ Соритрует массив таким образом, 
        что все элементы менше указанного элемента с index будут слева, 
        большие справа
        """
        mid = arr[index]
        left = []
        right = []
        for i, number in enumerate(arr):
                if number < mid:
                        left.append(number)
                elif number > mid:
                        right.append(number)
        
        sorted_arr = []
        sorted_arr.extend(left)
        sorted_arr.append(mid)
        sorted_arr.extend(right)
        dict = {
                "array": sorted_arr,
                "mid": mid,
                "index": len(left)
        }

        return dict


for i, number in enumerate(arr):
        dict = mysort(arr, i)
        if dict["index"] == m:
                print("array = ", dict["array"])
                print("mid = ", dict["mid"])