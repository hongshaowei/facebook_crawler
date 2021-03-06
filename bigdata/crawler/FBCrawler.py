'''
Created on 3 Sept. 2016
@author: casper
'''
import sys
import requests
import json
import facebook
#import MySQLdb

# from facepy import GraphAPI
#from nchc.bigdata.crawler.lib.util import Util

class FBCrawler:
    '''
    classdocs
    '''
    config = 'config'
    token = 'EAACEdEose0cBAHclE52vPvm7Nrf0hZBQWzC5NMEK8Qp6OVfdX9kMLZCq6V5YFZBI5QhsUzMpgqEz1K27ur5HpQy6BlGb20OAUt3JohtlWZAH6RMlLqlHMAvd6wPpTahatN86fZAIfcSMEFx7aZCjJ8RqZBkoymGpXpLQxdcsk0zUwZDZD'
    graph_url = 'https://graph.facebook.com/v2.7/'
    
    app_id = '1214654765221490'
    app_secret = '9a6f076128897979b7c66b1027319cfc'

    export_fo = None




    def __init__(self):
        token = self.getConfig()
        self.checkToken(token);

    def getConfig(self):
        fo = open(self.config, "r")
        self.token = fo.readline()
        fo.close()
        return self.token
    
    def checkToken(self, token):
        _url = FBCrawler.graph_url + 'tsaiingwen?access_token={}'.format(token)
        try:
            res = requests.get(_url)
            if res.status_code == 400 :
                self.token = self.get_fb_token()
                print(" renew token")
        except requests.exceptions.RequestException:
            print("error")
            
    def go_posts(self):
        _url = FBCrawler.graph_url + 'tsaiingwen?access_token={}&fields=posts{{comments{{like_count,message,shares,created_time,from,message_tags}}}}'.format(self.token)
        print(_url)
        res = requests.get(_url)
        jsondata = json.loads(res.text, encoding="utf-8")
        #print(jsondata['posts']['data'])
        return jsondata
    
    def go_comments(self, postID):
        _url = FBCrawler.graph_url +'{}/?access_token={}&fields=comments'.format( postID, self.token)
        res = requests.get(_url)
        jsondata = json.loads(res.text)
        print(jsondata)
        return jsondata['comments']['data']
    
    def get_fb_token(self):           
        payload = {'grant_type': 'client_credentials', 'client_id': self.app_id, 'client_secret': self.app_secret}
        file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
        #print file.text #to test what the FB api responded with    
        result = file.text.split("=")[1]
        #print file.text #to test the TOKEN
        fo = open(self.config, "w")
        fo.write(result)
        fo.close()
        return result
    
    def initExport(self):
        if self.export_fo is None:
             self.export_fo = open(Util.add_unique_postfix('.csv', 8), 'w')
    def export2File(self, json):
        return

    

crawler = FBCrawler()
token = crawler.get_fb_token()

json_posts = crawler.go_posts()
print(json_posts)

with open('data.json' , 'w' , encoding= 'utf-8') as f:
    json.dump(json_posts , f)

### crawl comments by the sepcial post
#json_comments = crawler.go_comments('232633627068_10155042036377069')
#for comment in json_comments:
#     print("id: {0}\nfrom: {1}".format(comment['id'], comment['from']['name']))