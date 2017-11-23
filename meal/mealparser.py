#-*-coding:utf-8-*-*-
#mealparser.py
import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from konlpy.tag import Twitter
import chardet
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

def answering_meal(question):
    #HTTP GET Request
    response = requests.get('http://www.uos.ac.kr/food/placeList.do')
    
    #print(response)
    #print(response.text)
    #html 소스 가져오기
    #html = req.text
    html = response.text
    #html = unicode(value,"utf-8", errors= "ignore")
    #BeautifulSoup으로 html소스를 python객체로 변환하기
    #첫 인자는 html소스코드, 두번쨰인자는 어떤 parser를 이용할지 명시.
    #이 글에서는 python 내장 html.parser를 이용했다
    soup = BeautifulSoup(html,'html.parser')
    
    #Css Selector를 통해 html요소들을 찾아낸다.
    #제목만
    my_titles = soup.select(
        '#day > table > tbody > tr > th'
        )
    my_menus = soup.select(
        '#day > table > tbody > tr > td'
    )
    #딕셔너리
    data = {}
    
    
    #my_titles는 list 객체
    for title, menu in zip(my_titles, my_menus):
        data[title.text.encode('utf-8')] = menu.text.encode('utf-8')
        #Tag안의 텍스트
        #print(title.text)
        #Tag의 속성을 가져오기(ex: href속성)
        #print(title.get('href'))
    
    jsonString = json.dumps(data)
    
    
    # return("다왓다")
    if u'조식' in unicode(question):
        print(data['조식'])
        return data['조식']
    elif u'중식' in unicode(question):
        return data['중식']
    elif u'석식' in unicode(question):
        return data['석식']    
    else:
        return "오늘의 조식은 " + data['조식'] + "\n중식은 " + data['중식'] + "\n석식은 " + data['석식'] + '입니다.' 
    
    # #http header가져오기
    # header = response.headers
    # #http status 가져오기
    # status = response.status_code
    # #http가 정상적으로 되었는지
    # is_ok = response.ok
    
    
'''    
def answering_etc(question):
    twitter = Twitter()
    #print "*************", chardet.detect(question)
    malist = twitter.pos(question,norm=True,stem=True)
    malist = np.char.encode(malist,'utf-8')
    print "*************", chardet.detect(malist[0,0])
    print "shape....", malist.shape
    temp = []
    for i in range(malist.shape[0]):
        temp.append(unicode(malist[i,0]))
    print temp[0]   
    x = [unicode("하영"),unicode("범우"),unicode("상진")]
    print "******************DDDDDDDDDDD",x
    return malist[0,0]
'''    