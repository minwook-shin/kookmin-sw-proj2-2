"""
20171628 서범석 assignment 5
재귀적 , 반복적 피보나치 수열의 시간 비교
"""
import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def interfibo(n):
    result = [0 , 1]

    for i in range(2 , n+1):
    	result.append(result[i-1] + result[i-2])
    return result[n]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
    	break
    ts = time.time()
    fibonumber = interfibo(nbr)
    ts = time.time() - ts
    print("InterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
