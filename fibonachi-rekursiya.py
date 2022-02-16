'''def find_fibonachi(N):
    if N <= 1:
        return N
    else:
        return(find_fibonachi(N-1)+find_fibonachi(N-2))


print(find_fibonachi(100))'''


"""def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

print(fib(1000000))"""


def even_numbers(list):
    dict = enumerate(list)
    a = 0
    for i, j in dict:
        if j%2==0:
            a+=1
    return a


def number_of_prime_numbers(list):
    number_prime = 0
    prime_list = [2,3,5,7]
    for i in list:
        if i<10:
            if i in prime_list:
                number_prime += 1
        else:
            d = 1
            while d*d <= i:
                d += 2
                if i%d == 0 or i%2 == 0:
                    break
                elif d*d>=i:
                    number_prime += 1     
    return number_prime



def count_of_numbers(list):
    count_numbers = []
    for i in list:
        number = enumerate(i)
        list_of_numbers = ['1','2','3','4','5','6','7','8','9','0']
        new_type_of_number = []
        for i, j in number:
            if len(new_type_of_number)<3:
                if j == ' ':
                    continue
                elif j == '.' and len(new_type_of_number)==0 or j == ',' and len(new_type_of_number)==0:
                    new_type_of_number.append('0')
                    new_type_of_number.append('.')
                elif j == '.' and len(new_type_of_number)>=1 or j == ',' and len(new_type_of_number)>=1:
                    new_type_of_number.append('.')
                elif j in list_of_numbers:
                    new_type_of_number.append(j)
            else:
                real_number = float(
                    new_type_of_number[0]+
                    new_type_of_number[1]+
                    new_type_of_number[2]
                )
                if real_number > 0.5:
                    count_numbers.append(real_number)
                break
    return len(count_numbers)







def how_much_thu(list):
    count_of_thu = 0
    for i in list:
        date = i.split()
        if date[0] == 'Thu':
            count_of_thu+=1
    return count_of_thu



import datetime


def how_much_thu(list):
    count_of_thu = 0
    for i in list:
        date = datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f')
        day_of_week = date.weekday()
        if day_of_week == 1:
            count_of_thu += 1
    return(count_of_thu)





from datetime import datetime, timedelta


def how_much_thu(list):
    count_of_thu = 0
    for i in list:
        date = datetime.strptime(i, '%m-%d-%Y')
        day_of_week = date.weekday()
        if day_of_week == 1:
            new_date = date + timedelta(days=7)
            if new_date.month != date.month:
                count_of_thu += 1
    return count_of_thu

