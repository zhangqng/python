import requests
import json
import bootstrap4
#Request URL
#每个钉钉群有一个唯一的access_token
url = 'https://oapi.dingtalk.com/robot/send?access_token=xxxx'
#Request Data
headers = {"Content-Type": "application/json ;charset=utf-8 "}
data = dict(
    msgtype = "text",
    text = {"content": "test"},
)
data = json.dumps(data)
#使用Requests发送Post请求
response = requests.post(url=url,data=data,headers=headers)
print(response.content)