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
import random

reload(sys)
sys.setdefaultencoding('utf-8')

def answering_etc(question):
    twitter = Twitter()
    #print "*************", chardet.detect(question)
    malist = twitter.pos(question,norm=True,stem=True)
    malist = np.char.encode(malist,'utf-8')
    
    silly_keyword = ['바보','멍청이','자살','닥치다','꺼지다','심심하다','미치다','병신','인정','자퇴','메롱','노답','경의중앙']
    malist_word = malist[:,0].tolist()
    
    #print "xxxxxxxxxxxxx", malist_word
    found_keyword = None
    for word in silly_keyword:
        print '**********', malist_word[0]
        if word in malist_word:
            found_keyword = word
            break;
        
            
    #print "ddddddddddddddddd", found_keyword
    if found_keyword == silly_keyword[0]:
        #바보
        return  "바보라니, 말이 심하시네. 이 멍청아" 
    elif found_keyword == silly_keyword[1]:
        #멍청아
        return "멍청아? 다시 청량리에 발도 못 붙일 줄 알아라"
    elif found_keyword == silly_keyword[2]:
        #자살
        return "학생상담센터는 학생회관 210호에 있습니다. 학생상담센터 전화번호는 02-6490-6270 입니다. 힘들때 언제든지 연락해주세요."
    elif found_keyword == silly_keyword[3]:
        #닥쳐
        return "입닥쳐 말포이!"
    elif found_keyword == silly_keyword[4]:
        #꺼져
        return "시스템을 종료합니다"
    elif found_keyword == silly_keyword[5]:
        #심심해
        return "우울한 코끼리와 놀아요~!!"
    elif found_keyword == silly_keyword[6]:
        #미친
        return "ㅋㅋㅋㅋ웅 ㅇㅋ"
    elif found_keyword == silly_keyword[7]:
        #병신
        return "ㅋ?"
    elif found_keyword == silly_keyword[8]:
        #인정
        return "어~인정~"
    elif found_keyword == silly_keyword[9]:
        #자퇴
        return "잘가ㅠㅠ 멀리 안나갈게~"
    elif found_keyword == silly_keyword[10]:
        #메롱
        return "혀 뽑는다."
    elif found_keyword == silly_keyword[11]:
        #노답
        return "아직 젊잖아요! 힘내요!"
    elif found_keyword == silly_keyword[12]:
        #경의중앙
        return "경의중앙선이 경의중앙했는데 무슨 문제라도..?"
    elif found_keyword == None:
        not_understand = ["뭐라구욧?","다시 한번 말씀해 주세요.","못 알아 듣겠어요.."]
        found_keyword = not_understand[random.randrange(0,len(not_understand))]
        return found_keyword