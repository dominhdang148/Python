from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sentece
import underthesea as uds


def index(request):
    template = loader.get_template('token.html')
    result=uds.word_tokenize("Xin chào các bạn")
    context={
        'y':result,
    }
    return HttpResponse(template.render(context,request))

 