import sys,requests,json

BaseUrl='http://api.e-stat.go.jp/rest/2.1/app/getStatsData?appId=b09e33724c5a0b1568a78b2598db83e8dd91bd94&lang=J&statsDataId=0003191320&metaGetFlg=Y&cntGetFlg=N&sectionHeaderFlg=1'

def GetData(url):
    result=requests.get(url)
    return result.text

if __name__=='__main__':
    data=GetData(BaseUrl)
    print(data)
