from sympy import *
import time

t=time.time()
theta1,theta2=symbols('theta1 theta2')
l1,l2,l3,x,y=symbols('l1 l2 l3 x y')

eq2=l2*sin(theta2)+(l1+l3)*sin(theta1)-y
eq1=l2*cos(theta2)+(l1+l3)*cos(theta1)-x

init_printing()

ans=solve([eq1,eq2],[theta1,theta2])
print(ans)
print(time.time()-t)