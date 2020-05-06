import requests
import re
import os
import sys
import json

# 视频AV号列表
aid_list = []

# 获取一个AV号视频下所有评论
def getAllCommentList(item):
    url = "http://api.bilibili.com/x/reply?type=1&oid=" + str(item) + "&pn=1&nohot=1&sort=0"
    r = requests.get(url)
    numtext = r.text
    json_text = json.loads(numtext)
    commentsNum = json_text["data"]["page"]["count"]
    print(commentsNum)
    # page = commentsNum // 20 + 1
    page = 100
    for n in range(1,page):
        url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn="+str(n)+"&type=1&oid="+str(item)+"&sort=1&nohot=1"
        req = requests.get(url)
        text = req.text
        json_text_list = json.loads(text)
        for i in json_text_list["data"]["replies"]:
            info_list.append([i["content"]["message"]])
    # print(info_list)

# 保存评论文件为txt
def saveTxt(filename,filecontent):
    filename = str(filename) + ".txt"
    for content in filecontent:
        with open(filename, "a", encoding='utf-8') as txt:
            txt.write(content[0].replace('\n','') + '\n\n')
        print("文件写入中")

if __name__ == "__main__":
    aid_list = [412935552]
    for item in aid_list:        
        getAllCommentList(item)
        saveTxt(item,info_list)
