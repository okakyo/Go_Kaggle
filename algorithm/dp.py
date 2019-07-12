import json,sys

# あらかじめ定義されたJsonの文字列は以下の通り

outputJson={
	"github":"okakyo",
    "twitter":"31415O_Kyo",
    "answer": "",
    "homepage": "https://okakyo.github.io/Introduction/"
}

def decript(enCodeString,rot):
    """
    ・暗号文をROTによって解読する関数
        (引数)   : 
            encodeScript : 暗号化された文字列(必須),
            rot          : 置き換えるまでの文字数（デフォルト：13）
        (返り値) ： 複合された文字列
    """
    ans=""
    for ch in enCodeString:
        ch=str(ch)
        if 'A' <= ch <= 'Z':
            ans += chr((ord(ch) - ord('A') + rot) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            ans += chr((ord(ch) - ord('a') + rot) % 26 + ord('a'))
        else:
            ans += ch
    return ans

def main():
    ROT=13
    inputKey=input("ROTで解読するキーを入力してください。")
    try:
        ROT=int(inputKey)%26
    except:
        pass
    print("ROT{}で暗号を復号化します。".format(ROT) if ROT!=0 else "平文で暗号を表示します。")
    inputString=input('文字列を入力してください。:')
    x=inputString
    if not inputString:
        # 入力されなかったら、そこで終了する
        print('必ず文字を入力してください。')
        sys.exit(1)
    answer=decript(x,ROT)
    outputJson["answer"]=answer
    return json.dumps(outputJson)

if __name__=="__main__":
    main()
    

