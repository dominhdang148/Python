from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Sentece
import underthesea as uds
import numpy as np
text=""
def result(request):
    template=loader.get_template('result.html')
    global text
    kq=np.array(uds.pos_tag(text))
    context={
        'kq':kq,
    }
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def add(request):
    global text
    text=request.POST['sent']
    return HttpResponseRedirect(reverse('result'))


    