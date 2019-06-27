culc="4 ? 4 ? 4 = -3"
qu=culc.split('=')[0]
ans=culc.split('=')[1]
print(type(qu))
after=qu.replace('?','+',1).replace('?','-',1)
print(after)
print(eval(after))
print(eval(after)==int(ans))