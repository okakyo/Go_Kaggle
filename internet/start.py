import requests,random,json,time
BASE_URL="https://apiv2.twitcasting.tv/internships/2019/games"
headers={
    "content-type": "application/json",
    'Authorization':'Bearer {}'.format("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjcwZmM5YzkzNTY5MTdlZTM3ZWMyNmE1YTYxN2Q1M2QwMzRmN2Q2OWE1ODJhMDgyZTY5MGYyYjBjMjJiNDk2MmNiOGM5MGI0YWViYjE1MDI2In0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6IjcwZmM5YzkzNTY5MTdlZTM3ZWMyNmE1YTYxN2Q1M2QwMzRmN2Q2OWE1ODJhMDgyZTY5MGYyYjBjMjJiNDk2MmNiOGM5MGI0YWViYjE1MDI2IiwiaWF0IjoxNTYxNjA5NjA0LCJuYmYiOjE1NjE2MDk2MDQsImV4cCI6MTU3NzE2MTYwNCwic3ViIjoiOTE4MzE1OTQwMTY0NDg1MTIwIiwic2NvcGVzIjpbInJlYWQiXX0.i2LyDqBAj4KP7g0Z5A2bowSac9JhB_AK-PotgmzweswZbDzb9lgaGV_Cv-KOZmMQ3c_f6VBNeEPPaTVWT411t13RSQqArsiq1rwhqLbJFRPuBDARdxBHX8jUw4NVYkz1fNfQ6I16McjPwC7JVFovRo-SytTIRGrJTJMja7NE8Nit9_Agx_WVRdTYmUZfN4p0z0v-Fq1iyakomAH6QssK1gwhE2tpL1YVjMLgMo7hUVTxweRJ65Jq7Vnq4uLl3Z1Z29IiGBz_uAFFWvlLhLqhaiTqmnJEHkh9x-ZR8T5Q8cJ33pt4_a_DehAAUw6oN6aXqvuXT7_uaqI29r6ViiQ4xg")
}
while(True):
    for i in range(3):
        getUrl=BASE_URL+"?level={}".format(i+1)
        data=requests.get(getUrl,headers=headers).json()
        ansID=data['id']
        question=data['question']
        qu,ansQ=question.split('=')
        ansQ=int(ansQ)
        for _ in range(10000):
            ans=""
            p=qu
            for _ in range(2*(i+1)):
                x=random.choice("+-*/")
                ans+=x
                p=p.replace(' ? ',x,1)
            if(eval(p)==ansQ):
                break
        comment=requests.post(BASE_URL+"/"+ansID,headers=headers,json={'answer':ans})
        continue
    print(comment.text)
    time.sleep(1)
        



    




