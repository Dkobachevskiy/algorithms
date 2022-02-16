def find_fibonachi(N):
    if N == 0:
        print('Error')
    elif N == 1:
        print(1)
    elif N == 2:
        print(1)
    elif N > 2:
        fibonachi_numbers = [1, 1, 2]
        for i in range(2, N-1):
            next_finachi = fibonachi_numbers[i-1] + fibonachi_numbers[i]
            fibonachi_numbers.append(next_finachi)
        print(fibonachi_numbers[N-1])

def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

print(fib(1000000))


find_fibonachi(100000)
