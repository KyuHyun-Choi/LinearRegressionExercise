# 불러와야 할 것 : 넘파이모듈, 사이킷런 데이터 셋, 판다스모듈
import numpy as np
from sklearn import datasets
import pandas as pd

# 당뇨데이터 베이스 로드
diabetes_dataset = datasets.load_diabetes()


# 가설함수 구현
def prediction(X, theta):
    return X @ theta


# 경사 하강법 구현
def gradient_descent(X, theta, y, iterations, alpha):  # X: 디자인 매트릭스, y: 목표 변수, iterations: 학습 횟수, alpha: 학습률
    m = len(X)  # 디자인 매트릭스 데이터 레코드의 수, 행의 수

    for _ in range(iterations):
        error = prediction(X, theta) - y  # 에러, 예측값과 목표변수의 차이
        theta = theta - alpha / m * (X.T @ error)  # 세타값은 선형회귀모델에서 당뇨병 입력변수 각각의 영향력

    return theta


X = diabetes_dataset.data  # 입력변수
y = diabetes_dataset.target  # 목표변수

theta = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  # 세타값 초기값을 모두 0으로 설정

prediction(X, theta)  # 목표변수와 세타값의 점곱

theta = gradient_descent(X, theta, y, 10, 0.01)  # 학습 횟수 : 10회, 학습률 : 0.01

print(theta)

#linear regression design matrix 판다스 데이터 프레임으로 보기좋게 정리
X = pd.DataFrame(diabetes_dataset.data, columns = diabetes_dataset.feature_names)
print(X)

#10가지 입력변수 나이, 성별, bmi, 평균혈압, T세포, ldl, hdl, 갑상선 자극 호르, 라모트리진, 혈당, 병의 진행상황 측정
print(diabetes_dataset.DESCR)