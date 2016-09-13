#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json, pyprind


# def parse_comment(i, token):
# 	req_for_posts = requests.get("https://graph.facebook.com/v2.5/{0}/comments?access_token={1}".format(i['id'], token))# api用post就會顯示該使用者的貼文的ID再加上comments就會顯示該篇貼文的評論
# 	postJson = json.loads(req_for_posts.text)
# 	# print(postJson)
# 	for j in postJson['data']:
# 		# print(j)
# 		f.write(str(j)+'\n')
# 		req_for_comments = requests.get("https://graph.facebook.com/v2.5/{0}/comments?access_token={1}".format(j['id'], token))#用該篇評論的id再接comments就會顯示該則回應底下的所有回應
# 		commentJson = json.loads(req_for_comments.text)
# 		for k in commentJson['data']:
# 			# print(k)
# 			f.write(str(k)+'\n')
# 			# detect_fake_user(k)


def parse_post(token):
	re = requests.get('https://graph.facebook.com/v2.5/46251501064_10153631427351065/?fields=comments.limit(100){message}&access_token=' + token)# api用post就會顯示該使用者的貼文s
	#if you want to chose a specific time span, append 'since=1420041600' after 'post?' 
	#cause it use Unix seconds, so 1420041600 means 2015/01/01
	jsonObj = json.loads(re.text)
	for i in jsonObj['comments']['data']:
		f.write(i['message']+'\n')
	re = requests.get(jsonObj['comments']['paging']['next'])
	jsonObj = json.loads(re.text)
	# print(jsonObj)
	while 'paging' in jsonObj:
		for i in jsonObj['data']:
			f.write(i['message']+'\n')
		if 'next' in jsonObj['paging']:
			re = requests.get(jsonObj['paging']['next'])
			jsonObj = json.loads(re.text)
		else:
			break

if __name__  ==  "__main__":
	with open('accessToken.txt','r',encoding='utf-8') as f:
		token = f.read()
	f = open('comment.txt', 'w', encoding='utf-8')
	parse_post(token)
	f.close()