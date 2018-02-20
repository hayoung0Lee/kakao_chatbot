# kakaobot view
# -*- coding: utf-8 -*-
# kakaobot 시작할때
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    #포스트 에러 방지
from django.shortcuts import redirect # redirect 
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect


@csrf_exempt
def initialization(message):
    
    if message == unicode(u'우울한 코끼리가 뭔가요?'): 
        return JsonResponse({
                    'message':{
                        "user_key": "encryptedUserKey",
                        'text': unicode(u'우울한 코끼리는 서울시립대학교 학생들을 대상으로한 챗봇 서비스입니다. 현재는 학식 정보 제공과 간단한 대화가 가능합니다. 학식에 대한 질문은 \'학식 알려줘\'와 같은 형식으로 입력해주세요.')
                    },
                    'keyboard':{
                        'type':'buttons',
                        'buttons':[ unichr(0x2753)+'우울한 코끼리가 뭔가요?',
                                    unichr(0x2753)+'사용법 알려주세요',
                                    unichr(0x2753)+'대화 시작하기']
                    }
        })
    elif message == unicode(u'사용법 알려주세요'): 
        return JsonResponse({
                    'message':{
                        "user_key": "encryptedUserKey",
                        'text': unicode(u'현재 우울한 코끼리는 학식 정보제공과 간단한 대화가 가능합니다. 학식이 궁금하실때는 \'학식 알려줘\'와 같은 형식으로 질문해주세요')
                    },
                    'keyboard':{
                        'type':'buttons',
                        'buttons':[ unichr(0x2753)+'우울한 코끼리가 뭔가요?',
                                    unichr(0x2753)+'사용법 알려주세요',
                                    unichr(0x2753)+'대화 시작하기']
                                    }
        })
    elif message == unicode(u'대화 시작하기'): 
        return JsonResponse({
                    'message':{
                        "user_key": "encryptedUserKey",
                        'text': unicode(u'자유로운 대화를 시작합니다. 아직 우울한 코끼리는 개발중이라서 똑똑하지 않아요. 조금만 이해해주세요!')
                    },
                    'keyboard':{
                        'type':'text'
                    }
        })
    else:
         return JsonResponse({
                    'message':{
                        "user_key": "encryptedUserKey",
                        'text': unicode(u'궁금하신 것 있나요?')
                    },
                    'keyboard':{
                        'type':'buttons',
                        'buttons':[ unichr(0x2753)+'우울한 코끼리가 뭔가요?',
                                    unichr(0x2753)+'사용법 알려주세요',
                                    unichr(0x2753)+'대화 시작하기']
                    }
        })
        