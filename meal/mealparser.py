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
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')


intent_list = OrderedDict({
    "식당" : {"식당":None,"알다":None},
    "학식" : {"학식":None,"알다":None},
    "동아리" : {"동아리":None,"추천":None},
    #"건물" : ["건물","알려"],
})
print "ORDER", intent_list.keys()[1]

story_slot_entity = OrderedDict({
    "식당":{"장소":None, "날짜":None},
    "학식":{"식당":None, "날짜":None, "시간":None},#시간: 조식, 중식, 석식
    "동아리":{"분과":None, "소속":None}, #동아리 분과, 동아리소속(중앙동아리 소모임)
})

#식당별 아침, 점심, 저녁 알려주기
#기본적으로 학관 정보 알려주기

def answering(answer):
    length = answer.__len__()
    position = answer[0:length-3]
    time = answer[length-2:length]
    
    #학관 1층, 아느칸, 자연과학관, 본관 8층, 생활관
    if position == unicode('학관 1층'):
        response = requests.get('http://www.uos.ac.kr/food/placeList.do')
    elif position == unicode('아느칸'):
        response = requests.get('http://www.uos.ac.kr/food/placeList.do?rstcde=030')
    elif position == unicode('자연과학관'):
        #return "죄송합니다. 자연과학관은 방학중 운영하지 않습니다. 학생식당을 이용해주세요." 
        response = requests.get('http://www.uos.ac.kr/food/placeList.do?rstcde=040')
    elif position == unicode('본관 8층'):
        response = requests.get('http://www.uos.ac.kr/food/placeList.do?rstcde=010')    
    elif position == unicode('생활관'):
        response = requests.get('http://www.uos.ac.kr/food/placeList.do?rstcde=050')
        
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    for br in soup.find_all("br"):
        br.replace_with("\n")
        
    #Css Selector를 통해 html요소들을 찾아낸다.
    #제목만
    my_titles = None
    my_menus = None
    
    if time ==unicode('아침'):
        my_titles = soup.select(
            '#day > table > tbody > tr:nth-of-type(1) > th'
        )
        my_menus = soup.select(
            '#day > table > tbody > tr:nth-of-type(1) > td'
        )
    elif time ==unicode('점심'):
        my_titles = soup.select(
            '#day > table > tbody > tr:nth-of-type(2) > th'
        )
        my_menus = soup.select(
            '#day > table > tbody > tr:nth-of-type(2) > td'
        )
    elif time ==unicode('저녁'):
        my_titles = soup.select(
            '#day > table > tbody > tr:nth-of-type(3) > th'
        )
        my_menus = soup.select(
            '#day > table > tbody > tr:nth-of-type(3) > td'
        )
    '''
    data = {}
    data[my_titles[0].text.encode('utf-8')] = my_menus[0].text.encode('utf-8')
    '''
    if(position==unicode('자연과학관')):
        return "죄송합니다. 자연과학관은 방학중 운영하지 않습니다. 학생식당을 이용해주세요." 
    if(len(my_titles) == 0):
        return "오늘의 " + position + '는 메뉴가 없습니다.'
    
    title = my_titles[0].text.encode('utf-8')
    menu = my_menus[0].text.encode('utf-8')
    menu = str.strip(menu)
    
    if not menu:
        return "오늘의 " + position + '는' + title +' 메뉴가 없습니다.'
    else:
        return "오늘의 " + position + ' ' + title + '은\n'+ menu + '\n\n입니다.' 
    

    
    

#기존
'''
def answering_all(malist):
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
    
    #식당 이름 -> db
    #print malist
    
    data ={}
    
    #my_titles는 list 객체
    for title, menu in zip(my_titles, my_menus):
        data[title.text.encode('utf-8')] = menu.text.encode('utf-8')
        #Tag안의 텍스트
        #print(title.text)
        #Tag의 속성을 가져오기(ex: href속성)
        #print(title.get('href'))
    
    jsonString = json.dumps(data)
    
    print "type", type(malist)
    # return("다왓다")
    if u'조식' in malist:
        print(data['조식'])
        return data['조식']
    elif u'중식' in malist:
        return data['중식']
    elif u'석식' in malist:
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