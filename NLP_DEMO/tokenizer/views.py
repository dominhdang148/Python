from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Sentece
import underthesea as uds
import numpy as np
from . import refdict as r
text = ""


def index(request):
    global kq
    kq = np.array(uds.ner(text))
    for word in kq:
        word[1] = r.pos_Dict[word[1]]
        word[2] = r.chunk_Dict[word[2]]
        word[3] = r.name_Dict[word[3]]
    # for word in kq:
    #     if word[3]=='O':
    #         word[3]=""  # Loại bỏ nhãn từ không có kết quả
    kqcssf = np.array(uds.classify(text),ndmin=1)
    context = {
        't': text,
        'kq': kq,
        'kqcssf': kqcssf,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def add(request):
    global text
    text = request.POST['sent']
    return HttpResponseRedirect(reverse('index'))
