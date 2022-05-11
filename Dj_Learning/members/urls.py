from django.urls import path
from members import views

urlpatterns = [path("", views.index, name='index'), ]
