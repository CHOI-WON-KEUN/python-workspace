'''
흡광율 실험 데이터를 통해 지시약의 pKa 값 결정하기
'''
import os
import numpy as np
from numpy.lib.arraypad import pad
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # pip install sklearn

sharps = 50

##### Data Frame ###################################
cwd = os.path.dirname( os.path.realpath(__file__) ) # 현재 파이썬 실행 파일의 경로
exl_file = os.path.join(cwd, 'absorbance.xlsx') # 엑셀 파일 경로(흡광율 데이터)
df = pd.read_excel(exl_file) # 엑셀 읽기. DataFrame 생성

print('\n#####', 'Absorbance', '#' * sharps)

df.rename(columns = {'Solution(pH)' : 'pH',
                     '436.4nm (HIn)': 'HIn',
                     '592.1nm (In-)': 'In-'}, inplace = True) # 컬럼명 변경
print(df)

X = np.array(df['pH'])
y = np.array(df['HIn'])

A = y[0]
y = y[1:-1]
X = X[1:-1]
print(X)
print(y)

b = 1
c = (0.02 * 0.5) / 1.5 / 1000
# print('c =', c)

# Epsilon_HIn 계산 # lambda_max = 436.4
eps_HIn = A / (b * c)
# print('epsilon_HIn =', eps_HIn)

# Beer-Lambert Law 적용
c_HIn = y / (eps_HIn * b) * 10**6
c_In_ = c * 10**6 - c_HIn
print('c_HIn\t\t:', c_HIn)
print('c_In_\t\t:', c_In_)

log_In_HIn = np.log10(c_In_ / c_HIn)

# Scatter 그래프 - 1
# plt.scatter(X, log_In_HIn)
# plt.title('Linear regression of log([In-] / [HIn]) vs. pH', pad=10)
# plt.xlabel('pH', labelpad=10)
# plt.ylabel('log([In-] / [HIn])', labelpad=10)
# plt.xticks(np.linspace(X[0], X[-1], 10))
# plt.yticks(np.linspace(log_In_HIn[0], log_In_HIn[-1], 10))
# plt.grid(linestyle='-', color='0.1', linewidth=0.5)
# plt.show()

# 첫 번째 실험 데이터가 abnormal하여 제거한다.
X = X[1:]
log_In_HIn = log_In_HIn[1:]

# Scatter 그래프 - 2
plt.scatter(X, log_In_HIn)
plt.title('Linear regression of log([In-] / [HIn]) vs. pH', pad=10)
plt.xlabel('pH', labelpad=10)
plt.ylabel('log([In-] / [HIn])', labelpad=10)
plt.xticks(np.linspace(X[0], X[-1], 10))
plt.yticks(np.linspace(log_In_HIn[0], log_In_HIn[-1], 10))
plt.grid(linestyle='-', color='0.1', linewidth=0.5)
# plt.show()

# 선형 회귀
line_fitter = LinearRegression()
line_fitter.fit(X.reshape(-1, 1), log_In_HIn)
inclination = line_fitter.coef_[0]    # 기울기 
y_intercept = line_fitter.intercept_  # y 절편
x_intercept = -y_intercept / inclination # x 절편

print('기울기\t\t:', inclination)
print('y절편\t\t:',  y_intercept)
print('x절편\t\t:',  x_intercept)

# Scatter 그래프 + Regression Line
tx = np.linspace(X[0], X[-1], 2) # X의 범위
ty = np.linspace(X[0] * inclination + y_intercept, X[-1] * inclination + y_intercept, 2) # 회귀직선으로 구한 y의 범위
plt.plot(tx, ty, 'g-')
plt.show()