import requests
from dotenv import load_dotenv
import os
import random,json
import time
SetCulc="+-*/"
postURL="	https://apiv2.twitcasting.tv/internships/2019/games/"
load_dotenv()

headers={
    "content-type": "application/json",
    'Authorization':'Bearer {}'.format(os.environ.get('AUTH_TOKEN'))
}
while(True):
   
    for i in range(1,4):
        getUrl="https://apiv2.twitcasting.tv/internships/2019/games?level={}".format(i)
        data=requests.get(getUrl,headers=headers).json()
        
        ansID=data['id']
        question=data['question']
        qu,ansQ=question.split('=')
        
        ansQ=int(ansQ)
        
        while(True):
            ans=""
            p=qu
            for _ in range(2*i):
                x=random.choice(SetCulc)
                ans+=x
                p=p.replace('?',x,1)
            if(eval(p)==ansQ):
                break
       
        comment=requests.post(postURL+ansID,headers=headers,json={'answer':ans})
        print(comment.text)
        continue
    print('終了します.')
    time.sleep(5)
        



    




