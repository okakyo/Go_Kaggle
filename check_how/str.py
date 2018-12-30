#これでパスワードの自動生成を代わりにやってくれる。

import random,string
X=string.ascii_letters+string.digits

for i in range(1000):
    ans=''
    for i in range(8):
        ans+=random.choice(X)
    print(ans)