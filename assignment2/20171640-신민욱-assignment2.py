"""
Name: 과제 – Factorial 계산
• 키보드로 숫자 입력
• Factorial 계산하여 출력
• ‐1을 입력할 때까지 반복함
"""


def factorial(num):  # 모듈로 묶어 줍니다.
    """펙토리얼 계산 모듈"""
    basic = 1  # 1을 기본으로 할당합니다.
    if num == 0:  # 0은 1로 출력하게 처리합니다.
        return 1  # 1을 반환합니다.
    while num > 0:  # num을 1까지 돌립니다.
        basic *= num  # 전에 할당한 1과 입력된 n을 곱합니다.
        num -= 1  # num에 1을 차감합니다.
    return basic  # 통과된 while문의 basic을 아래 코드로 반환해줍니다.


try:  # 예외 처리를 위한 시작
    while True:  # 무한으로 돌립니다.
        IN_NUM = int(input("Enter a number:"))  # 입력을 받습니다.
        if IN_NUM == -1:  # -1을 입력했을 때
            break
        else:  # -1을 입력하지 않았을 때
            print(factorial(IN_NUM))
except ValueError:  # int가 아닌 값은 예외처리합니다.
    print("숫자가 아닙니다.")