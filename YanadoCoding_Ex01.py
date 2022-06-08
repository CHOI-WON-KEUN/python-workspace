########################################
# 1차시 수업 학습 목표
# 1. 변수와 데이터형
# 2. 연산자
# 3. 제어문
#    - 조건문 : if
#    - 반복문 : for
# 4. 함수
# 5. 재귀함수
########################################

########################################
# 1. 변수와 데이터형
#  1) 숫자, 문자, 콜렉션(리스트, 집합, 튜플, 사전), 클래스
#  2) 동적 데이터 타입

c = 32
print(type(c))
c = 32.0
print(type(c))

# 다양한 데이터 타입
print(type(3), type(3.14), type('3'), type(1+2j), type(True), type([1]), type((1,)), type({1}), type({1:'id'}))


########################################
# 2. 연산자
#  1) 사칙연산(+, -, * , /), 정수 나누기(//), 나머지(%), 지수(** )
#  2) 관계 연산자(>, <, >=, <=, ==, !=)
#  3) 논리 연산자(and, or, not)
#  4) 불(Bool)
#  5) 연산자 오버로딩

# 연산자 사용
print(9-3, 8*2.5, 9/2, 9/-2, 9%2, -9%2, 9//2, 4+3*5, (4+3)*5, 3>2, 'SSHS', sep='\t', end='\n\n')

# 지수 연산
print(2**10, 2**-1)

# 복소수 연산
print((1 + 2j) + (2 - 3j), (1 + 2j) * (2 - 3j))

# 연산자 오버로딩 : +
print('Seoul Science' + ' ' + 'High School')

# 연산자 오버로딩 : *
print('*' * 30)


########################################
# 3. 제어문
#  1) 조건문 : if
#  2) 반복문 : for

# 윤년 : 2월달이 29일까지 있는 해.
# 매 4년마다 돌아오지만, 그 중 100년이 되는 해는 윤년이 아니면서, 다시 400년이 되는 해
# 년도가 4로 나누어지고 100으로 나누어지면 안됨.
# 1번의 조건과 상관없이 400으로 나누어지면 윤년.
# 예 : 1년(X), 4년(O), 100년(X), 400(O)

#윤년 판단 함수 : 3가지 버전
def isLeapYear(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False

def isLeapYear1(y):
    if y % 400 == 0:
        return True
    elif y % 4 == 0:
        if y % 100 != 0:
            return True
        else:
            return False
    else:
        return False

def isLeapYear2(y):
    if y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

#윤년 판단 함수 호출
print(isLeapYear(1), isLeapYear(4), isLeapYear(100), isLeapYear(400))

# 사용자 입력으로 윤년 판단
# y = int(input('Year : '))
# print(isLeapYear(y))
    
# 문자열 삼각형 출력 - 1
# *
# **
# ***
# ****
# *****
# ******
# *******

# 반복문을 통한 문자열 삼각형 출력-1
for k in range(1, 8):
    print('*' * k)


print() # 줄 바꿈

# 문자열 삼각형 출력 - 2
# *******
# ******
# *****
# ****
# ***
# **
# *

# 반복문을 통한 문자열 삼각형 출력-2
for k in range(7, 0, -1):
    print('*' * k)


########################################
# 5. 재귀함수
#  1) factorial
#   f(n) = 1         , if n = 1
#        = n × f(n−1), if n > 1
 
#  2) fibonacci
#   fib(n) = 0, if n = 0
#          = 1, if n = 1
#          = fib(n−2) + fib(n−1), if n > 1

# factorial 재귀함수
def f(n):
    if n < 2:
        return 1
    return n * f(n - 1)

# factorial 결과 확인
print(f(5), f(361), sep='\n')

# fibonacci 재귀함수
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

# fibonacci 결과 확인
for i in range(20):
    print(fib(i), end='__')


########################################
# 과제 - 1 : 구구단 출력
# 1) 1개단의 구구단 출력   : 반복문 사용
# 2) 전체단의 구구단 출력  : 중첩 반복문 사용
# 3) 함수 이용 구구단 출력 : 1)을 함수로 구현 후 반복 호출


# python -m pip install --upgrade pip   ## pip upgrade


# 추가 사전 학습
import pandas as pd
import numpy  as np
import matplotlib 
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1024)
sin_x = np.sin(x)
cos_x = np.cos(x)
plt.plot(x, sin_x, 'r')
plt.plot(x, cos_x, 'b')
plt.show()
