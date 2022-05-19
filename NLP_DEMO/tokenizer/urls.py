from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index, name='index'),
    path('index/add/',views.add, name="add"),
    path('result',views.result,name='result')
]