#-*-coding:utf-8-*-*-
#의도 분류 하는 스크립트
import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import chardet
import numpy as np
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')

 
output_data = ""

#의도 구분을 위한 학습 data
intent_list = OrderedDict({
    "식당" : {"식당":None,"알다":None},
    "학식" : {"학식":None,"알다":None},
    "동아리" : {"동아리":None,"추천":None},
    #"건물" : ["건물","알려"],
})

story_slot_entity = OrderedDict({
    "식당":{"장소":None, "날짜":None},
    "학식":{"식당":None, "날짜":None, "시간":None},#시간: 조식, 중식, 석식
    "동아리":{"분과":None, "소속":None}, #동아리 분과, 동아리소속(중앙동아리 소모임)
})

def analizing(malist):
    for i in range(malist.shape[0]):
        malist[i,0] = unicode(malist[i,0])
    
        
    #print "EEEEE", malist[0,0]
    #intent_list에 있는 단어가 모두 포함되어있으면 그 인텐트로 분류한다
    check_intent = {}
    intent_code = 0
    #intent_code: 0-학식 1-식당 2-동아리 3-그외
    intent_in = False
    
    #for문을 개선해야할 것 같음
    for intent in intent_list.values():
        #print "DDDDDDDDDDDD", intent
        for tag in intent.keys():
            if tag in malist[:,0]:
                intent[tag] = True
            else:
                intent[tag] = False
           
        if False not in intent.values():
            return intent_code
        else:
            intent_code += 1
        
    
    return intent_code
        