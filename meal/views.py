# meal view
# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    #포스트 에러 방지
import json
import mealparser

'''
def keyboard(request):
    return JsonResponse({
        'type':'text',
        #'buttons':[ 'kenyoung','beomwoo','hayoung','sangjin']
    })
'''

@csrf_exempt
def message(request, result):
    e = request.session.get('result')
    print "I'm in meal views", result

    answer = mealparser.answering_meal(message)
    
    return JsonResponse({
        'message':{
            'text': unicode(answer)
        },
        'keyboard':{
            'type': 'text'
            #"type": "buttons",            
            #"buttons":[ '날씨','사용법','처음으로','소개']
        }
    })
    
    