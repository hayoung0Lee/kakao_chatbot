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

def keyboard(request):
    return JsonResponse({
        'type':'text',
        #'buttons':[ 'kenyoung','beomwoo','hayoung','sangjin']
    })

#intent_code: 0-학식 1-날씨 2-동아리 3-그외    

@csrf_exempt
def message(request):
    
    #문자 인코딩 해결하는부분 여기는 건들지 말것
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content']
    user_key = return_json_str['user_key'] # user_key
    type = return_json_str['type']
    if input_type == 'photo':
        return JsonResponse({
            'message':{
                'text': unicode("아직 사진을 인식하는 기능은 없어요 :'(")
            },
        })
    
    #처리부분 들어갈곳
    intent_code = in_analize.analizing(return_str)
 
    if intent_code == 0:    #intent가 학식
        return redirect(reverse('meal_message', kwargs={ 'result': return_str }))
    elif intent_code == 1:  #날씨 
        return JsonResponse({
            'message':{
                'text': unicode("날씨 알림 기능을 준비중 입니다.")
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
        answer = sillyparser.answering_etc(return_str)
        return JsonResponse({
            'message':{
                "user_key": "encryptedUserKey",
                'text': unicode(answer)
            },
            'keyboard':{
                'type':'text'
            }
        })
    