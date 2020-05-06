import lxml
import requests
import time
import sys
import json

YOUTUBE_IN_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&pageToken={pageToken}&videoId={videoId}&key={key}'
YOUTUBE_LINK = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&order=relevance&videoId={videoId}&key={key}'
key = ''   #改为自己申请的google api
	

def commentExtract(videoId, count = -1):
	print ("\nComments downloading")
	#关闭http连接，增加重连次数


	page_info = requests.get(YOUTUBE_LINK.format(videoId = videoId, key = key))
	while page_info.status_code != 200:
		if page_info.status_code != 429:
			print ("Comments disabled")
			sys.exit()

		time.sleep(20)
		page_info = requests.get(YOUTUBE_LINK.format(videoId = videoId, key = key))
	page_info = page_info.json()
	comments = []
	co = 0;
	for i in range(len(page_info['items'])):
		#对3000赞以上的评论进行保留，可以根据需求更改
        # if page_info['items'][i]['snippet']['topLevelComment']['snippet']['likeCount']>=0:
		if 0==0:
			comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
			co += 1
		if co == count:
			return comments

	# INFINTE SCROLLING
	while 'nextPageToken' in page_info:
		temp = page_info
		page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = videoId, key = key, pageToken = page_info['nextPageToken']))

		while page_info.status_code != 200:
			time.sleep(20)
			page_info = requests.get(YOUTUBE_IN_LINK.format(videoId = videoId, key = key, pageToken = temp['nextPageToken']))
		page_info = page_info.json()

		for i in range(len(page_info['items'])):
			comments.append(page_info['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'])
			co += 1
			if co == count:
				return comments
	print ()

	return comments

if __name__ == '__main__':
    commit = commentExtract("IRzplsoYm0M")
    # commit = commentExtract("FjHJk2JYTHs")
    with open("commits\\youtube.txt", "w", encoding="utf-8") as f:    
        for i in commit:
            f.write(i)
