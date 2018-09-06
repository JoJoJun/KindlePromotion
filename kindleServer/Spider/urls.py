from Spider import  views
from django.conf.urls import url, include
urlpatterns = [

    url(r'^spider/', views.hello, name='hello'),
    url(r'^$',views.main, name='hello2' )
]