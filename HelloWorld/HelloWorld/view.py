# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
	context = {}
	context['hello'] = '你好 !'
#	return HttpResponse("Hello World !")
	return render(request, 'hello.html', context)
