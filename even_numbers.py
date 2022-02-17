from random import randint

"""Сколько четных чисел в этом столбце?"""
def even_numbers(list):
    dict = enumerate(list)
    a = 0
    for i, j in dict:
        if j%2==0:
            a+=1
    return a

list_even = list(range(2,1001,2))
list_odd = list(range(1,1000,2))

list_numbers = list_even + list_odd

print(even_numbers(list_numbers))
