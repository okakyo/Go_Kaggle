k,s=map(int,input().split())
ans=0
for i in range(k+1):
    for j in range(k+1):
        if (s-i-j>=0 and s-i-j<=k):ans+=1
print(ans)
