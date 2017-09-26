"""
조합의 수
–Cf(n,k)은 팩토리얼을 사용한 방법의 결과를 보여줌
–C(n,k)은 재귀함수로 사용한 결과를 보여줌
"""


def factorial(n):
    """팩토리얼"""
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
    return result


def cf(n, k):
    """팩토리얼 사용한 조합의 수"""
    return factorial(n) / (factorial(k) * factorial(n - k))


def c(n, k):
    """재귀함수 사용한 조합의 수"""
    if k == 0:
        return 1
    elif n < k:
        return 0
    else:
        return c(n - 1, k - 1) + c(n - 1, k)


# 입력받기
try:
    in_n = int(input("enter n:"))
    in_k = int(input("enter k:"))
except:
    print("int please!")
else:  # 출력하기
    print(int(c(in_n, in_k)))
    print(int(cf(in_n, in_k)))
