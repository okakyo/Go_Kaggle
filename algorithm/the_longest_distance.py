from  math import sqrt

N=int(input())
X,Y=[],[]
ans=0
for i in  range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
for i in range(len(X)):
    for j in range(i,len(X)):
        ans=max(ans,sqrt(pow(X[i]-X[j],2)+pow(Y[i]-Y[j],2)))
        
print(ans)
