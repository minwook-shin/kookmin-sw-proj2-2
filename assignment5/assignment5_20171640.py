"""
과제 – 피보나치 수열 (반복 기법, iterative)
"""

# 시간 측정 모듈
import time


def fibo(n):
    """피보나치 수열을 재귀 함수로 구현하는 코드"""
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def iterfibo(n):
    """피보나치 수열을 반복적으로 구현하는 코드"""
    fibo_bools = True
    one = 1
    two = 1
    while n > 2:
        if fibo_bools:
            one = one + two
        else:
            two = one + two
        fibo_bools = not fibo_bools
        n -= 1
    if fibo_bools:
        return two
    else:
        return one


# 재귀적으로 구현한 버전과 수행 시간 비교를 위한 코드
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
