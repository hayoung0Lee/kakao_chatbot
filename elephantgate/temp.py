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

#prev_slot_value = None
output_data = ""

#의도 구분을 위한 학습 data
intent_list = {
    "학식" : ["학식","알려"],
    "날씨" : ["날씨","알려"],
    "동아리" : ["동아리","추천"],
    #"건물" : ["건물","알려"],
}

#각 의도별 slot구성
story_slot_entity = {
    "학식":{"식당":None, "날짜":None, "시간":None},#시간: 조식, 중식, 석식
    "날씨":{"장소":None, "날짜":None},
    "동아리":{"분과":None, "소속":None}, #동아리 분과, 동아리소속(중앙동아리 소모임)
}

#intent도출
intent_id = "학식"
intent_code = 0
intent_done = False
slot_value = story_slot_entity.get(intent_id)

#NER도출
#학식에 대해서, 학교 식당 list
#양식당이 아느칸, 학생회관1층이 학생식당
cafe_list = ['학생회관1층','양식당','자연과학관','본관8층','생활관']
date_list = ['오늘','내일','모래']
time_list = ['조식','중식','석식']

def analizing(question):
    twitter = Twitter()
    #print "*************", chardet.detect(question)
    malist = twitter.pos(question,norm=True,stem=True)
    malist = np.char.encode(malist,'utf-8')

    #global prev_slot_value
    #global slot_value
    
    #if first_depth == True:
    #dictionary기반 slot구성
    for tag in malist:
        if (tag[1] in ['Noun']):
            if tag[0] in cafe_list:
                slot_value['식당'] = tag[0]
                #print tag[0]
            elif tag[0] in date_list:
                slot_value['날짜'] = tag[0]
                #print tag[0]
            elif tag[0] in time_list:
                slot_value['시간'] = tag[0]
                #print tag[0]
    #print "111111111",story_slot_entity.get('학식')
    
    if None in slot_value.values():
        key_values = ""
        for key in slot_value.keys():
            if(slot_value[key] is None):
                key_values = key_values + key + ","
        output_data = key_values + "선택해주세요"
        intent_done = False
    else:
        output_data = "학식을 알려드리겠습니다."
        intent_done = True
    print output_data
    
    #prev_slot_value = slot_value
    #print prev_slot_value
    return [intent_code,intent_done,output_data]

    '''
    else:
        slot_value = prev_slot_value
        for tag in malist:
            if (tag[1] in ['Noun']):
                if tag[0] in cafe_list:
                    slot_value['식당'] = tag[0]
                    #print tag[0]
                elif tag[0] in date_list:
                    slot_value['날짜'] = tag[0]
                    #print tag[0]
                elif tag[0] in time_list:
                    slot_value['시간'] = tag[0]
        
        if None in slot_value.values():
            key_values = ""
            for key in slot_value.keys():
                if(slot_value[key] is None):
                    key_values = key_values + key + ","
            output_data = key_values + "선택해주세요"
            intent_done = False
        else:
            output_data = "학식을 알려드리겠습니다."
            intent_done = True
        print output_data
        
        prev_slot_value = slot_value
        return [intent_code,intent_done,output_data]
    '''