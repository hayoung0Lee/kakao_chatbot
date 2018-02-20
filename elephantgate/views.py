# elephant gate view
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    #포스트 에러 방지
from django.shortcuts import redirect # redirect 
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
import in_analize
import sillyparser
from konlpy.tag import Twitter
import MySQLdb
from datetime import datetime
import jpype
import numpy as np
from threading import Thread
from . import initial


#to start project: sudo service mysql start

twitter = Twitter()
malist = None

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':[ unichr(0x2753)+'우울한 코끼리가 뭔가요?',
                    unichr(0x2753)+'사용법 알려주세요',
                    unichr(0x2753)+'대화 시작하기']
    })

#intent_code: 1-학식 0-식당 2-동아리 3-그외    

@csrf_exempt
def message(request):
    
    #문자 인코딩 해결하는부분 여기는 건들지 말것
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    user_key = return_json_str['user_key'] # user_key
    input_type = return_json_str['type']
    # 시간확인
    now_time = datetime.today().strftime("%Y%m%d%H%M%S")
    #MySQL
    db = MySQLdb.connect(host='localhost',user='root',passwd='',db='chatbot',charset='utf8')
    cur = db.cursor()
    #insert query
    insert = ("""insert into usertable (userkey,time,content) values (%s,%s,%s)""")
    #data
    data = (user_key,now_time,return_str)
    #insert data to db
    cur.execute(insert,data)
    #db commit
    db.commit()
    #cur.execute('select * from usertable')
    
    for row in cur.fetchall():
        print row[0],row[1],row[2],row[3]
    db.close()
    
    if input_type == 'photo':
        return JsonResponse({
            'message':{
                'text': unicode("아직 사진을 인식하는 기능은 없어요 :'(")
            },
            'keyboard':{
                'type':'text'
            }
        })
    jpype.attachThreadToJVM() #스레드 시작
    
    length = return_str.__len__()
    if return_str[0] == unichr(0x2753):
        return initial.initialization(return_str[1:length])    
    
    #이모티콘으로 분류할때
    #이모티콘으로 시작하는 경우는 버튼입니다
    #학식 / 동아리/
    #이모티콘 확인: https://github.com/gaqzi/django-emoji/blob/master/emoji/_unicode_characters.py
    #unichr(0x0001f48b)으로 쓴다, u'\u2049' -> 0x2049
    #문자가 아닌 character로 시작하는 경우 모두 이경우로 보낸다.
    #학식 문자
    elif return_str[0] == unichr(0x0001f374):
        #only fork and knife -> meal_time needed -> intent 학식:1 , time_needed:1 => 11
        #fork and knife + clock -> meal_done -> intent 학식:1 , time_needed:0 => 10
        
        if return_str[1] == unichr(0x0001f550):
            return redirect(reverse('meal_message', kwargs={ 'result': 10 , 'answer': return_str[2:length]}))
        else:
            return redirect(reverse('meal_message', kwargs={ 'result': 11, 'answer': return_str[1:length]}))
   
    #어느 이모티콘으로도 시작하지 않을때 처리
    #속도 개선 필요
    else:    
        #처리부분 들어갈곳
        
        malist = twitter.pos(return_str,norm=True,stem=True)
        malist = np.char.encode(malist,'utf-8')
        
        intent_code = in_analize.analizing(malist)
        
        
        if intent_code == 1:    #intent가 학식
            #처음에는 학관 학식을 먼저 알려주고 질의하기
            return redirect(reverse('meal_message', kwargs={ 'result': malist, 'answer': return_str}))
        elif intent_code == 0:  #식당 
            return JsonResponse({
                'message':{
                    'text': unicode("식당 알림 기능을 준비중 입니다.")
                },
                'keyboard':{
                    'type':'text'
                }
            })
        elif intent_code == 2:  #동아리 추천 
            return JsonResponse({
                'message':{
                    'text': unicode("동아리 추천 기능을 준비중 입니다.")
                },
                'keyboard':{
                    'type':'text'
                }
            })
        else:   #헛소리
            #여기서 농담 처리하기
            answer = sillyparser.answering_etc(malist)
            return JsonResponse({
                'message':{
                    "user_key": "encryptedUserKey",
                    'text': unicode(answer)
                },
                'keyboard':{
                    'type':'text'
                }
            })
    jpype.detachThreadFromJVM() #스레드 제거(core dump 오류 방지)
    