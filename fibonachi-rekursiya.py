def find_fibonachi(N):
    if N <= 1:
        return N
    else:
        return(find_fibonachi(N-1)+find_fibonachi(N-2))


print(find_fibonachi(100))
