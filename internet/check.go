package main

import (
  "net/http"
  "fmt"
  "io/ioutil"
  "encoding/json"
  "bytes"
   "time"
   "math/rand"
   "strings"
   "go/types"
   "go/token"
   "strconv"
   
)


type GetJson struct {
	Id   string    `json:"id"`
	Question string `json:"question"`
}

var BaseURL string ="https://apiv2.twitcasting.tv/internships/2019/games"


func getQuestion(level int) (string, string){
	lv:=strconv.Itoa(level)
	url :=BaseURL+"?level="+lv
	req,err:=http.NewRequest("GET",url,nil);
	if err != nil {
		fmt.Println(err)
		
	}
	req.Header.Add("content-type", "application/json")
	req.Header.Set("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjcwZmM5YzkzNTY5MTdlZTM3ZWMyNmE1YTYxN2Q1M2QwMzRmN2Q2OWE1ODJhMDgyZTY5MGYyYjBjMjJiNDk2MmNiOGM5MGI0YWViYjE1MDI2In0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6IjcwZmM5YzkzNTY5MTdlZTM3ZWMyNmE1YTYxN2Q1M2QwMzRmN2Q2OWE1ODJhMDgyZTY5MGYyYjBjMjJiNDk2MmNiOGM5MGI0YWViYjE1MDI2IiwiaWF0IjoxNTYxNjA5NjA0LCJuYmYiOjE1NjE2MDk2MDQsImV4cCI6MTU3NzE2MTYwNCwic3ViIjoiOTE4MzE1OTQwMTY0NDg1MTIwIiwic2NvcGVzIjpbInJlYWQiXX0.i2LyDqBAj4KP7g0Z5A2bowSac9JhB_AK-PotgmzweswZbDzb9lgaGV_Cv-KOZmMQ3c_f6VBNeEPPaTVWT411t13RSQqArsiq1rwhqLbJFRPuBDARdxBHX8jUw4NVYkz1fNfQ6I16McjPwC7JVFovRo-SytTIRGrJTJMja7NE8Nit9_Agx_WVRdTYmUZfN4p0z0v-Fq1iyakomAH6QssK1gwhE2tpL1YVjMLgMo7hUVTxweRJ65Jq7Vnq4uLl3Z1Z29IiGBz_uAFFWvlLhLqhaiTqmnJEHkh9x-ZR8T5Q8cJ33pt4_a_DehAAUw6oN6aXqvuXT7_uaqI29r6ViiQ4xg")
	
	client := new(http.Client)
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
	}
	defer resp.Body.Close()
	byteArray, _ := ioutil.ReadAll(resp.Body)

	var classes GetJson
	err = json.Unmarshal(byteArray, &classes)
	if err!=nil {
		fmt.Println(err)
	}
	
	return classes.Id, classes.Question
}

func PostQuestion(id string, ans string) (string){
	url := BaseURL+"/"+id
	answer:=`{"token":"` + ans +`"}"` 
	req,err:=http.NewRequest( "POST", url, bytes.NewBuffer([]byte(answer)))
	if err != nil {
		fmt.Println(err)
	}
	req.Header.Add("content-type", "application/json")
	req.Header.Set("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjcwZmM5YzkzNTY5MTdlZTM3ZWMyNmE1YTYxN2Q1M2QwMzRmN2Q2OWE1ODJhMDgyZTY5MGYyYjBjMjJiNDk2MmNiOGM5MGI0YWViYjE1MDI2In0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6IjcwZmM5YzkzNTY5MTdlZTM3ZWMyNmE1YTYxN2Q1M2QwMzRmN2Q2OWE1ODJhMDgyZTY5MGYyYjBjMjJiNDk2MmNiOGM5MGI0YWViYjE1MDI2IiwiaWF0IjoxNTYxNjA5NjA0LCJuYmYiOjE1NjE2MDk2MDQsImV4cCI6MTU3NzE2MTYwNCwic3ViIjoiOTE4MzE1OTQwMTY0NDg1MTIwIiwic2NvcGVzIjpbInJlYWQiXX0.i2LyDqBAj4KP7g0Z5A2bowSac9JhB_AK-PotgmzweswZbDzb9lgaGV_Cv-KOZmMQ3c_f6VBNeEPPaTVWT411t13RSQqArsiq1rwhqLbJFRPuBDARdxBHX8jUw4NVYkz1fNfQ6I16McjPwC7JVFovRo-SytTIRGrJTJMja7NE8Nit9_Agx_WVRdTYmUZfN4p0z0v-Fq1iyakomAH6QssK1gwhE2tpL1YVjMLgMo7hUVTxweRJ65Jq7Vnq4uLl3Z1Z29IiGBz_uAFFWvlLhLqhaiTqmnJEHkh9x-ZR8T5Q8cJ33pt4_a_DehAAUw6oN6aXqvuXT7_uaqI29r6ViiQ4xg")
	client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println(err)
    }
    defer resp.Body.Close()
	byteArray, _ := ioutil.ReadAll(resp.Body)
    return string(byteArray)
}

func solveProblem(level int ,question string)(string){
	CulcOperator:="+-*/"
	ans:=""
	for i := 0; i < len(question); i++ {
		// iの値が0から9まで変化していく
		if(string(question[i])=="?"){
			rand.Seed(time.Now().UnixNano()) // 乱数のシードとして現在時刻のナノ秒を渡す
			i := rand.Intn(len(CulcOperator)) // 0 ～ 配列の要素数までのランダム値取得
			op:=string(CulcOperator[i])
			ans +=op
		}
		
	} 
	return ans
}

func main(){
	for i := 1; i < 4; i++ {
		// iの値が0から9まで変化していく
		id,getQuestion:=getQuestion(i)
		Q:=strings.Split(getQuestion,"=")
		question,getAns:=Q[0],Q[1]
		ans,_:=strconv.Atoi(getAns)
		fmt.Println(id,ans)
		for{
			ans:=solveProblem(i,question)
			fset := token.NewFileSet()
			result,err:=types.Eval(fset,nil,token.NoPos,ans)
			if(err!=nil){
				fmt.Println(err);
			}
			fmt.Println(ans)
			fmt.Println(result)
		}
	} 

}