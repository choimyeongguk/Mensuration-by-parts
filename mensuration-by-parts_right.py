import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import numpy as np

## 함수 선언 ##
def fc(x):
 return x**2

## 변수 선언 ##
spot1, spot2 = map(float, input('범위 입력(정수 정수) : ').split())
x, y = [], []
x_bar, y_bar = [], []
l = spot2 - spot1
max, min = fc(spot1), fc(spot1)
S=0

## 메인 코드 ##
for i in np.arange(spot1-l*0.2, spot2+l*0.2, 0.01):
 x.append(i)  # 정의역
 y.append(fc(i))  # 치역
 if(i>max):
  max = fc(i)  # 최댓값
 if(i<min):
  min = fc(i)  # 최솟값
y_range = max - min
x.append(spot2)
y.append(fc(spot2))

plt.ion()  # 그래프에 애니메이션 적용
for n in range(0, 101):  # 함수를 0~100개로 나눔
 for i in range(0, n):  # n개 만큼 박스 생성
  plt.plot(x, y, color='red', linewidth='1')  # 원함수 그리기
  if(spot1-l*0.2<=0<=spot2+l*0.2):
   plt.plot([0, 0], [min-y_range*0.2, max+y_range*0.2], color='black')  # y축 그리기
  plt.plot([spot1-l*0.2, spot2+l*0.2], [0, 0], color='black')  # x축 그리기
  num = '#0055ff' if i%2==0 else '#00aaff'  # 홀짝마다 박스 색깔 다르게 설정
  if(spot1+(spot2-spot1)/n*i<=0):
    plt.gca().add_patch(ptch.Rectangle((spot1+(spot2-spot1)/n*i, 0),(spot2-spot1)/n, fc(spot1+(spot2-spot1)/n*i), color=num))  # 박스 생성
  else:
    plt.gca().add_patch(ptch.Rectangle((spot1+(spot2-spot1)/n*i, 0),(spot2-spot1)/n, fc(spot1+(spot2-spot1)/n*(i+1)), color=num))  # 박스 생성
  S = S + abs(1/n*fc(spot1+(spot2-spot1)/n*i))  # 넓이 계산
 plt.title('n=%d, area= %f'%(n, S))  # 계산값 출력
 plt.draw()  # 그래프 표시
 plt.pause(0.1)  # 0.1초 지연
 plt.clf()  # 그래프 초기화
 S=0  # 넓이 초기화
plt.show()
