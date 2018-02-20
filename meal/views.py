# meal view
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    #포스트 에러 방지
import json
import mealparser
import numpy as np
from ast import literal_eval
from emoji import Emoji

'''
def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        "buttons":[ '학관 1층 학식 알려줘','아느칸 학식 알려줘','자연과학관 학식 알려줘','본관 8층 학식 알려줘', '생활관 학식 알려줘']
    })
'''

cafe_list = ['학생회관1층','양식당','자연과학관','본관8층','생활관']
date_list = ['오늘','내일','모래']
time_list = ['조식','중식','석식']

@csrf_exempt
def message(request, result, answer):
    #result = request.session.get('result')
    
    

    #result = np.array(literal_eval(unicode(result)))
    
    if result == '10':
        #버튼해제, 아침 점심 저녁 따로 알려주기
        answer = mealparser.answering(answer)
        #print(1)
        return JsonResponse({
            'message':{
                'text': unicode(answer)
            },
            
            'keyboard':{
                'type': 'text',
            }
        })
    elif result == '11':
        #버튼으로 아침, 점심, 저녁 물어보기
        #처리할 데이터는 어느 관인지,
        #print(2)
        return JsonResponse({
            'message':{
                'text': unicode(u'언제의 학식 정보를 알려드릴까요?')
            },
            
            'keyboard':{
                'type': 'buttons',
                #unichr(0x0001f48b)
                "buttons":[ unichr(0x0001f374)+unichr(0x0001f550)+unicode(answer)+' 아침',
                            unichr(0x0001f374)+unichr(0x0001f550)+unicode(answer)+' 점심',
                            unichr(0x0001f374)+unichr(0x0001f550)+unicode(answer)+' 저녁',
                            unichr(0x2753)+'처음으로',
                           ]
            }
        })
    else:
        #print(3)
        return JsonResponse({
            'message':{
                'text': unicode(u'학식은 학관 1층, 아느칸, 자연과학관, 본관 8층, 생활관에서 먹을 수 있어요. 어느 관의 학식 정보를 알려드릴까요?\n\n')
                +unicode(u'학식 말고 시립대 근처 맛집은 궁금하시지 않나요? ')
            },
            
            'keyboard':{
                'type': 'buttons',
                #unichr(0x0001f48b)
                "buttons":[ unichr(0x2753)+'처음으로',
                            '맛집 알려줘',    
                            unichr(0x0001f374)+'학관 1층',
                            unichr(0x0001f374)+'아느칸',
                            unichr(0x0001f374)+'자연과학관',
                            unichr(0x0001f374)+'본관 8층',
                            unichr(0x0001f374)+'생활관',
                           ]
                
                
            }
            
        })
        
    