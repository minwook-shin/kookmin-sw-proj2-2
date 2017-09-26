''' 과제 Assignment 4
조합의 수를 구하여라 (팩토리얼,재귀함수) '''


def factorial(n):  # 팩토리얼을 나타낸 함수
    number = 1
    for i in range(1, n + 1):
        number *= i
    return number


def Cf(n, m):  # 팩토리얼을 이용한 조합의 수
    return factorial(n) / (factorial(m) * factorial(n - m))


def C(n, m):  # 재귀함수를 이용한 조합의 수
    if n == 0 and not m == 0:
        return 0
    elif m == 0:
        return 1
    else:
        return C(n - 1, m) + C(n - 1, m - 1)


while True:  # Main 파일
    try:
        n = int(input('Enter n :'))
        if n == -1:  # 탈출코드
            break
        m = int(input('Enter M :'))
        if n < m:  # 조합에서는 m이 n보다 클 수 없음
            print("n must bigger than m or equal m ok?")
            continue
    except:
        print('n or m must be integer!!')
    else:
        print("CF(", n, ',', m, ") = ", Cf(n, m))
        print("C(", n, ',', m, ") = ", C(n, m))
