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
import jpype
#from gensim.models import Word2Vec
import gensim.models.keyedvectors as Word2Vec

reload(sys)
sys.setdefaultencoding('utf-8')

def answering_etc(malist):
   
	#형태소로 바꾸기	
    silly_keyword = ['바보','멍청이','자살','닥치다','꺼지다','심심하다','미치다','병신','인정','자퇴','메롱','노답','중앙','거지','휴강','드랍','혼밥','뚝배기','탕진','시발','실화','공강','학고','재수강','ㅗ','웅','하이','피방','극혐','열공','휴학','안녕','배고파','뭐','맛집','우울하다','그만하다','코끼리']
    malist_word = malist[:,0].tolist()
    
    #print "xxxxxxxxxxxxx", malist_word
    found_keyword = None
    #print unicode(malist[0])
    for word in silly_keyword:
        if word in malist_word:
            found_keyword = word
            break;
        
            
    #print "ddddddddddddddddd", found_keyword
    if found_keyword == silly_keyword[0]:
        # 바보
        return  "바보라니, 말이 심하시네. 이 멍청아" 
    elif found_keyword == silly_keyword[1]:
        # 멍청아
        return "멍청아? 다시 청량리에 발도 못 붙일 줄 알아라"
    elif found_keyword == silly_keyword[2]:
        # 자살
        return "학생상담센터는 학생회관 210호에 있습니다. 학생상담센터 전화번호는 02-6490-6270 입니다. 힘들때 언제든지 연락해주세요."
    elif found_keyword == silly_keyword[3]:
        # 닥쳐
        return "입닥쳐 말포이!"
    elif found_keyword == silly_keyword[4]:
        # 꺼져
        return "시스템을 종료합니다"
    elif found_keyword == silly_keyword[5]:
        # 심심해
        return "우울한 코끼리와 놀아요~!!"
    elif found_keyword == silly_keyword[6]:
        # 미친
        return "ㅋㅋㅋㅋ웅 ㅇㅇ"
    elif found_keyword == silly_keyword[7]:
        # 병신
        return "ㅋ?"
    elif found_keyword == silly_keyword[8]:
        # 인정
        return "어~인정~"
    elif found_keyword == silly_keyword[9]:
        # 자퇴
        return "잘가요ㅠㅠ 멀리 안나갈게요~"
    elif found_keyword == silly_keyword[10]:
        # 메롱
        return "혀 뽑는다."
    elif found_keyword == silly_keyword[11]:
        # 노답
        return "아직 젊잖아요! 힘내요!"
    elif found_keyword == silly_keyword[12]:
        # 경의중앙
        return "경의중앙선이 경의중앙했는데 무슨 문제라도..?"
    elif found_keyword == silly_keyword[13]:
        # 거지
        return "무지개반사!!"
    elif found_keyword == silly_keyword[14]:
        # 휴강
        return "최고의 강의는 휴강bb"
    elif found_keyword == silly_keyword[15]:
        # 드랍
        return "멀어지는 졸업.."
    elif found_keyword == silly_keyword[16]:
        # 혼밥
        return "혼밥이 디폴트입니다! 떼밥이 유별난 거예요!"
    elif found_keyword == silly_keyword[17]:
        # 뚝배기
        return "여기서 뚝배기는 머리입니다"
    elif found_keyword == silly_keyword[18]:
        # 탕진
        return "돈쓰는게 제일 재밌어!!"
    elif found_keyword == silly_keyword[19]:
        # 시발
        return "예쁜말을 씁시다"
    elif found_keyword == silly_keyword[20]:
        # 실화
        return "예 실화입니다."
    elif found_keyword == silly_keyword[21]:
        # 공강
        return "월공강이 최고!"
    elif found_keyword == silly_keyword[22]:
        # 학고
        return "학고를 받으면 다음 학기 수강신청이 14학점 이하로 제한되어요ㅠㅠ"
    elif found_keyword == silly_keyword[23]:
        # 재수강
        return "C+이하 과목에 한하여 재수강할 수 있어요~"
    elif found_keyword == silly_keyword[24]:
        # ㅗ
        return "ㅗ"
    elif found_keyword == silly_keyword[25]:
        # 웅
        return "아구 착하다 쓰담쓰담"
    elif found_keyword == silly_keyword[26]:
        # 하이
        return "ㅎㅇㅎㅇ"
    elif found_keyword == silly_keyword[27]:
        # 피방
        return "피방ㄱㄱ"
    elif found_keyword == silly_keyword[28]:
        # 극혐
        return "ㄹㅇ"
    elif found_keyword == silly_keyword[29]:
        # 열공
        return "내일부터 열공해야지..!!"
    elif found_keyword == silly_keyword[30]:
        # 휴학
        return "휴학 신청은 대학행정정보시스템에서 가능해요!"
    elif found_keyword == silly_keyword[31]:
        # 안녕
        return "안녕하세요! 저는 우울한 코끼리입니다"
    elif found_keyword == silly_keyword[32]:
        # 배고파
        return "'학식 알려줘'라고 말씀해보세요!"
    elif found_keyword == silly_keyword[33]:
        # 뭐해
        return "저는 여러분께 더 좋은 서비스를 드리기 위해서 진화중이에요! 조금만 더 기다려주시면 더 똑똑한 우울한코끼리가 될게요 :)"
    elif found_keyword == silly_keyword[34]:
        # 맛집
        return "조만간 기가막힌 맛집을 추천해줄게요!"
    elif found_keyword == silly_keyword[35]:
        # 우울하다
        return "우울한 코끼리는 우울해"
    elif found_keyword == silly_keyword[36]:
        # 그만
        return "가지마세여ㅠㅠ"
    elif found_keyword == silly_keyword[37]:
        # 코끼리
        return "코끼리 중에 우울한 코끼리가 최고!"
    elif found_keyword == None:
        #word 2 vec실습
        '''
        train_data = [malist_word]
        print(train_data)
        
        model = Word2Vec(size=50, window=2, min_count=1)
        model.build_vocab(train_data)
        model.train(train_data,total_examples=model.corpus_count)
        print("model check : {0}".format(model))
        '''
        
        #http://w.elnn.kr/search/?query=%EC%95%88%EB%85%95-%EC%84%9C%EC%9A%B8%2B%EC%9D%BC%EB%B3%B8
                
        
        not_understand = ["뭐라구욧?","다시 한번 말씀해 주세요.","못 알아 듣겠어요..","우울한 코끼리는 아직 개발단계라서 이해하지 못하였습니다.","ㅇㅅㅇ?"]
        found_keyword = not_understand[random.randrange(0,len(not_understand))]
        
        # return 'checking'
        return found_keyword