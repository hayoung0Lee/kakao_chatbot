#meal_url
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'keyboard/',views.keyboard, name='meal_keyboard'),
        url(r'message/(?P<result>[^\/]*)/(?P<answer>[^\/]*)$',views.message, name='meal_message'),
    ]
