#meal_url

from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'meal^keyboard/',views.keyboard),
        url(r'^keyboard/',views.keyboard),
        url(r'^message',views.message),
        '''
        url(r'meal/keyboard/',views.keyboard),
        url(r'meal/^message',views.message),
    ]
