#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json,xlwt

token = 'EAACEdEose0cBAEEDMKKKS94gZAFEnTSoYSuTZCSw6dFIjdKkcIsn7In5zfsUJfZCp47iDs1tqqhR4sl7bwvRSwDeOb1sWEy7ClvTIFuz9NmShBHRYSXh6xD8ZB9dZCWFgutVy0AxZAPziwFxKOozAqrowO8JFZBItuhM2bfw6r1sgZDZD'

res = requests.get('https://graph.facebook.com/v2.3/tsaiingwen/posts?comments&access_token=%s'%(token))

jsonObj = json.loads(res.text)

with open('demo.json', 'w', encoding='utf-8') as f:
	json.dump(jsonObj, f)

# wbk = xlwt.Workbook()
# sheet = wbk.add_sheet('sheet 1')

# x=1
# post_id= 0
# ID=1
# name = 2
# message = 3
# message_id = 4
# created_time = 5

# for i in jsonObj['data']:
# 	for j in i['comments']['data']:
# #		sheet.write(x,post_id,j['id'])
# #		sheet.write(x,ID,j['from']['id'])
# 		sheet.write(x,name,j['from']['id'])
# 		sheet.write(x,message,j['message'])
# 		sheet.write(x,message_id,j['id'])
# 		sheet.write(x,created_time,j['created_time'])
# 		x=x+1
# wbk.save('test.xls')
# #		print(j['id'],j['like_count'],j['created_time'])
# #		print(j['from']['name'],j['from']['id'])
# #		print(j['message'])
# #		print(' ')

# #with open('data.json' , 'w' , encoding= 'utf-8') as f:
# #	json.dump(jsonObj , f)