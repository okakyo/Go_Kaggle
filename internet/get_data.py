import subprocess

data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8'
                                ,errors="backslashreplace").split("\n")
profiles=[i.split(":")[1][1:] for i in data if "All User Profile" in i]
for i in profiles:
    try:
        result=subprocess.check_output(['netsh','wlan','show','profiles'].decode('utf-8')
                                ,errors="backslashreplace".split("\n"))
        [i.split(":")[1][1:] for i in result if "Key Content" in i]
        try:
            print('{:<30}|{:<}'.format(i,result[0]))
        except IndexError:
            print('{:<30}|{:<}'.format(i,""))
    except subprocess.CalledProcessError:
        print('{:<30}|{:<}'.format(i,"Encoding Error! "))
