#elephantgate_url
# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from . import views
#app_name = 'elephantgate' apps.py 
#파일에 있는데 어떤 코드에서 여기에 추가하기도 하길래 일단 해놓음

urlpatterns = [
        url(r'^keyboard/',views.keyboard),
        url(r'^message',views.message),
        url(r'^meal/',include('meal.urls')),
        
    ]