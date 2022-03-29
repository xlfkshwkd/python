
def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return print(ret)

n=int(input("정수 n 입려해 거기까지 곱한다 "))

factorial(n)

#3