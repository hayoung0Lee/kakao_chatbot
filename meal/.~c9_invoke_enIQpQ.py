# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    #포스트 에러 방지
import json
import mealparser

def keyboard(request):
    return JsonResponse({
        'type':'text',
        #'buttons':[ 'kenyoung','beomwoo','hayoung','sangjin']
    })
    
@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    
    if unicode(return_str) == u'소개':  #유니코드로 비교할것
        return JsonResponse({
            'message':{
                'text':"우울한 코끼리입니다. 현재 서비스를 준비중입니다."  
            },
            # 'keyboard':{
            #     'type':'buttons',
            #     'buttons':[ 'kenyoung','beomwoo','hayoung','sangjin']
            # }
            'keyboard':{
                'type':'text'
            }
        })
    elif u'학식' in unicode(return_str):
        answer = mealparser.answering_meal(return_str)
        return JsonResponse({
            'message':{
                'text': unicode(answer)
            },
            'keyboard':{
                'type':'text'
            }
        })
    else:
        answer = mealparser.answering_etc(return_str)
        return JsonResponse({
            'message':{
                'text': answer
            },
            # 'keyboard':{
            #     'type':'buttons',
            #     'buttons':[ 'kenyoung','beomwoo','hayoung','sangjin']
            # }
            'keyboard':{
                'type':'text'
            }
        })
    
