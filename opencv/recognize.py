from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .classes import TextPrint

def index(request):
    return render(request,'test/index.html')

def click(request):
	forma = TextPrint(3)
	context ={}
	textf = forma.text 
	context['value1'] = textf
	return render(request , 'test/index.html' , context)