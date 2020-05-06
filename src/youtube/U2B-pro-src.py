import time
comments = []

with open("U2B-src\\u2-src.html","r",encoding="utf-8") as f:
    lines = f.readlines()      #读取全部内容 ，并以列表方式返回
    for line in lines:
        start = line.find('<yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">')
        if start != -1:
            end = line[start:].find('</yt-formatted-string>')
            word = line[start+110:start+end]
            print(word)
            # time.sleep(1)
        # print(line)
        # time.sleep(1)