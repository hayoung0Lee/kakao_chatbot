#-*-coding:utf-8-*-*-
#의도 분류 하는 스크립트
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

 
output_data = ""

#의도 구분을 위한 학습 data
intent_list = {
    "학식" : ["학식","알려"],
    "날씨" : ["날씨","알려"],
    "동아리" : ["동아리","추천"],
    #"건물" : ["건물","알려"],
}

def analizing(question):
    twitter = Twitter()
    #print "*************", chardet.detect(question)
    malist = twitter.pos(question,norm=True,stem=True)
    malist = np.char.encode(malist,'utf-8')

    
    
    for i in range(malist.shape[0]):
        malist[i,0] = unicode(malist[i,0])
    
        
    #print "EEEEE", malist[0,0]
    
    #intent_list에 있는 단어가 모두 포함되어있으면 그 인텐트로 분류한다
    check_intent = []
    intent_code = 0
    #intent_code: 0-학식 1-날씨 2-동아리 3-그외
    
    intent_in = False
    for intent in intent_list.values():
        check_intent = []
        print "intent check", intent
        intent_in = False
        for i in intent:
            for j in range(malist.shape[0]):
                if i == malist[j,0]:
                    intent_in = True
            check_intent.append(intent_in)
            
        if False not in check_intent:
            return intent_code
        else:
            intent_code += 1

    print intent_code
    return intent_code
        