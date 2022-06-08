########################################
# 3차시 수업 학습 목표
# 1. 라이브러리
#    - numpy
#    - pandas
#    - matplotlib.pyplot
#    - seaborn
#    - itertools
# 2. 멱집합(Power Set) 구하기
# 3. 설곽 작명소
########################################

########################################
# 1. 라이브러리
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

# Permutation 함수 구현
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

pool = ['1', '2', '3']
perm_result = permute(pool)
print('permute function ', perm_result)

# itertools.permutations 사용법
print('itertools.permutations', list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print('itertools.permutations(2)', list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

# 2차원 배열 생성
listA = [[1, 2, 3], [4, 5, 5]]
print('List A :', type(listA))
print(listA)
print(listA * 2) # 리스트 원소가 중복 추가됨.

arrA = np.array(listA)
print('Array A :', type(arrA), arrA.shape)
print(arrA)

arrB = np.array([-1, 0, 2, -1, 1, 3]).reshape(3, 2)
print('Array B :', type(arrB), arrB.shape)
print(arrB)
print(arrB * 2) # 행렬 각 항에 곱셈

arrC = arrA @ arrB # 행렬 곱셈
print('Array C :', type(arrC), arrC.shape)
print(arrC)

# 전체 항목 중 (최대값, 최소값, 합계, 평균)
print(np.max(arrC), np.min(arrC), np.sum(arrC), np.mean(arrC))

# 행(axis=0) 또는 열(axis=1) 중 (최대값, 최소값, 합계, 평균)
print(np.max(arrC, axis=0), np.min(arrC, axis=1), np.sum(arrC, axis=0), np.mean(arrC, axis=1))

# 정렬
print(np.sort(arrC))
print(np.sort(arrC, axis=0))
print(np.sort(arrC, axis=1))

# 행렬식, 역행렬, 고유값, 단위행렬
print('행렬식', np.linalg.det(arrC))
print('역행렬', np.linalg.inv(arrC))
print('고유값', np.linalg.eig(arrC))
print('단위행렬', np.eye(5))

# NationalNames.csv 분석하기
# 1880~2014 미국 신생아 이름 목록
names = pd.read_csv('./NationalNames.csv', header=0, names=['id','name','year','gender','births'])
print(names.head()) # 첫 5행 출력
print(names.count()) # 각 컬럼별 개수
print()

total_births = names.pivot_table('births', index='year', columns='gender', aggfunc=sum)
print(total_births.head(10))
print()

# 그래프 출력
# plt.title('Total births by gender and year')
# plt.plot(total_births)
# plt.show()

nm = names # 별칭
nm_group = nm.groupby(['year', 'gender']).size() # 년도별, 성별로 묶어 갯수 집계
print(nm_group.tail())

nm_dec = nm.groupby(['gender', nm['year'] // 10 * 10]).size() # 성별, 10년 단위별로 묶어 갯수 집계
print(nm_dec.head())

print(nm_dec.unstack())

# sns.set_style('whitegrid') # 차트 배경 설정
# sns.distplot(nm_dec.unstack(0), color='y')
# plt.show()

########################################
# 2. 멱집합(Power Set) 구하기
def powerSet1(S):
    PS = []
    for i in range(2 ** len(S)):
        n = i
        j = 1
        T = []
        while n > 0:
            if n % 2 == 1:
                T.insert(0, S[len(S) - j])
            n //= 2
            j += 1
        PS.append(T)
    return PS

def powerSet2(S):
    if len(S) == 0:
        return [set()]
    ss = powerSet2(S[1:])
    return [s | set(S[0]) for s in ss] + [s for s in ss]

def powerSet3(S):
    return [[S[j] for j in range(len(S)) if n & 2 ** j != 0] for n in range(2 ** len(S))]

Set = ['A', 'B', 'C', 'D']
# print(powerSet1(Set))
# print(powerSet2(Set))
# print(sorted(powerSet3(Set)))

# print([[j for j in range(len(Set)) if n & 2 ** j != 0] for n in range(2 ** len(Set))])


########################################
# 3. 설곽 작명소
# 2014년~2021년 입학생 명단 분석
# 동명이인의 끝에 붙은 알파벳 제거
# 설곽 입시생의 성비는?
# 가장 많은 학생 이름 10위?
# 가장 많은 성씨 10위?
# 설곽 입학생스러운 이름 추천?

from collections import Counter

df = pd.read_excel('./namesSSHS.xlsx')
print(df.info()) # 정보 확인
print(df.head()) # 첫 5개 데이터 조회
print('Column Names:', df.columns) # 컬럼명

df.set_index('교번', inplace=True) # 교번을 인덱스로 설정(인덱스는 고유값이어야 함)
print(df.tail()) # 마지막 5개 데이터 조회

print('\n이름 뒤에 붙은 알파벳 제거하기')
dupName = df[df['이름'].str.endswith('A')]
print(dupName.head()) # A가 이름 뒤에 붙은 명단 출력

transTable = str.maketrans('ABCD', '    ') # 이름에 붙은 알파벳을 제거하기 위한 사전(dict)
df['이름'] = [n.translate(transTable).strip() for n in df['이름']]
print(df.loc[[17031, 17032]]) # 인덱스로 조회. 2개 이상일 경우 인자를 리스트(list)로 전달한다.

print('\n최다 빈도 이름 10가지')
print(Counter(df['이름']).most_common(10)) # 가장 많은 이름 10개

nameList = list(df['이름']) # 이름 컬럼을 리스트로 저장
df['fName'] = [n[0] for n in nameList] # 성(? 성이 두 글자 고려 안함)
df['mName'] = [n[1] for n in nameList] # 이름 가운데 글자
df['lName'] = [n[2] if len(n) > 2 else ' ' for n in nameList] # 이름 마지막 글자(외자인 경우 공백)

print(df.head()) # 첫 5개 데이터 조회

topNo = 10 # 상위 랭킹 개수
arr1 = list(dict(Counter(df['fName']).most_common(topNo)).keys())
arr2 = list(dict(Counter(df['mName']).most_common(topNo)).keys())
arr3 = list(dict(Counter(df['lName']).most_common(topNo)).keys())

print(arr1) # 성 상위 랭킹
print(arr2) # 이름 가운데 글자 상위 랭킹
print(arr3) # 이름 마지막 글자 상위 랭킹

df2 = pd.DataFrame({'n1':arr1, 'n2':arr2, 'n3':arr3})
print(df2)

# for f in arr1:
#     for m in arr2:
#         for l in arr3:
#             print(f + m + l, end=', ')

nameSet = { arr1[np.random.randint(topNo)] +
            arr2[np.random.randint(topNo)] +
            arr3[np.random.randint(topNo)] for n in range(topNo ** 3) }

print('랜덤 이름 개수 :', len(nameSet))
print(nameSet)