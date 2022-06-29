import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def fc(x):
 return x**2

n = int(input('나누는 수 입력 : '))
spot1, spot2 = map(float, input('범위 입력(\'정수 정수\'로 입력) : ').split())
RorL = input("r or l? : ")
S = 0
x = []
y = []
l = spot2 - spot1
max = fc(spot1)
min = fc(spot1)

for i in np.arange(spot1-l*0.2, spot2+l*0.2, 0.01):
 x.append(i)
 y.append(fc(i))
 if(i>max):
  max = fc(i)
 if(i<min):
  min = fc(i)

y_range = max-min

if(spot1-l*0.2<=0<=spot2+l*0.2):
  plt.plot([0, 0], [min, max], color='black')
plt.plot([spot1-l*0.2, spot2+l*0.2], [0, 0],color='black')
plt.plot(x, y, color='red', linewidth='1')

if(RorL=='l'):
  for i in range(0, n):
    num = '#0055ff' if i%2==0 else '#00aaff'
    if(spot1+(spot2-spot1)/n*i>0):
      plt.gca().add_patch(patches.Rectangle((spot1+(spot2-spot1)/n*i, 0), (spot2-spot1)/n, fc(spot1+(spot2-spot1)/n*i), color=num))
    else:
      plt.gca().add_patch(patches.Rectangle((spot1+(spot2-spot1)/n*i, 0), (spot2-spot1)/n, fc(spot1+(spot2-spot1)/n*(i+1)), color=num))
    S = S + abs(1/n*fc(i/n))
else:
  for i in range(0, n):
    num = '#0055ff' if i%2==0 else '#00aaff'
    if(spot1+(spot2-spot1)/n*i>0):
      plt.gca().add_patch(patches.Rectangle((spot1+(spot2-spot1)/n*i, 0), (spot2-spot1)/n, fc(spot1+(spot2-spot1)/n*(i+1)), color=num))
    else:
      plt.gca().add_patch(patches.Rectangle((spot1+(spot2-spot1)/n*i, 0), (spot2-spot1)/n, fc(spot1+(spot2-spot1)/n*i), color=num))
    S = S + abs(1/n*fc(i/n))

print("\n%d %d"%(max, min))
plt.title('f(x)=x^2, n= %d, area : %f'%(n,S))
plt.show()