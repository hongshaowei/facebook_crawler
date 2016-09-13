#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json,xlwt

token = 'EAACEdEose0cBAFCqF5tXg5CNG8QZCGQKDxiLOM5oUvKZBJDsZByW08WHZBtuwnTPCZATTjKplprZCHbv2wfygsL7VGPvZBmPK41FGwrj2vxX2hvV3y6I03xefpK4kQCM91BlnzmJXBmDaP4ZB72arZBecPjAPjZAtM4jl54B8vbohjxwZDZD'

res = requests.get('https://graph.facebook.com/v2.3/tsaiingwen/posts?comments&access_token=%s'%(token))

jsonObj = json.loads(res.text)

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

x=1
post_id= 0
ID=1
name = 2
message = 3
message_id = 4
created_time = 5

for i in jsonObj['data']:
	for j in i['comments']['data']:
#		sheet.write(x,post_id,j['id'])
#		sheet.write(x,ID,j['from']['id'])
		sheet.write(x,name,j['from']['id'])
		sheet.write(x,message,j['message'])
		sheet.write(x,message_id,j['id'])
		sheet.write(x,created_time,j['created_time'])
		x=x+1
wbk.save('test.xls')
#		print(j['id'],j['like_count'],j['created_time'])
#		print(j['from']['name'],j['from']['id'])
#		print(j['message'])
#		print(' ')

#with open('data.json' , 'w' , encoding= 'utf-8') as f:
#	json.dump(jsonObj , f)