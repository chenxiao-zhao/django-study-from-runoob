# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

# from django.http import HttpResponse#from django.http import HttpRespon
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
