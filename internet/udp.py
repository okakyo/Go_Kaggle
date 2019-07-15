import requests
import json

formURL="https://sso.doshisha.ac.jp/auth/Login"
setURL='https://duet.doshisha.ac.jp/gakusei/html/fb/fb010/FB01001G.html'


Headers={'Date': 'Sun, 14 Jul 2019 05:24:40 GMT', 
        'Server': 'Apache', 'X-Frame-Options': 'deny',
        'X-XSS-Protection': '1; mode=block',
        'X-Content-Type-Options': 'nosniff',
        'Set-Cookie': 'JSESSIONID=28BFBA912BEA147782858C16AD26B239; Path=/gakusei/; HttpOnly; Secure, front-server=front-http2; Path=/; HttpOnly; Secure',
         'Cache-Control': 'no-cache, no-store', 'Expires': '-1', 'Pragma': 'no-cache', 
        'Content-Type': 'text/html;charset=UTF-8', 'Content-Language': 'ja', 
        'Content-Encoding': 'gzip', 'Vary': 'Accept-Encoding',
        'Transfer-Encoding': 'chunked', 'Connection': 'Keep-alive', 
        'Via': '1.1 ID-0002262072457544 uproxy-2'}

sendData={
    "usr_name":"cgub4065",
    "usr_password":"d6r5Wz8u"
}

html=requests.post("https://sso.doshisha.ac.jp/cgi-bin/portal.cgi",data=sendData)

print(html.text)
print(html.status_code)