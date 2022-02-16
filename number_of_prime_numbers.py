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


list_numbers = [i for i in range(1,100000)]

print(number_of_prime_numbers(list_numbers))
