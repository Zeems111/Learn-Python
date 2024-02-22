def fib(n):
    farr = [1] * (n+1)
    print(f'Call fib({n})')
    for i in range(2, n+1):
        farr[i] = farr[i-1] + farr[i-2]
    return farr[n-1]

if __name__ == '__main__':
    print(fib(7))