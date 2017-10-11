"""
20171646 안희운 assignment 5
재귀함수로 구현한 피보나치 수열
vs 반복문으로 구현한 피보나치 수열
"""
import time
import random


def fibo(n):
    """재귀함수로 구현한 피보나치 수열"""
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def interfibo(n):
    """반복문으로 구현한 피보나치 수열"""
    i = 2
    list = [0, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    while 1 < i < n + 1:
        fn = list[i - 2] + list[i - 1]
        list.append(fn)
        i += 1
    return list[n]


while True: #Main
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    tt = time.time()
    interfibonumber = interfibo(nbr)
    tt = time.time() - tt
    print("InterFibo(%d)=%d, time %6f" % (nbr, interfibonumber, tt))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
