from random import randint

"""Сколько четных чисел в этом столбце?"""
def even_numbers(list):
    dict = enumerate(list)
    a = 0
    for i, j in dict:
        if j%2==0:
            a+=1
    return a

lst = [randint(0, 1000) for i in range(1000000)]

print(even_numbers(lst))
