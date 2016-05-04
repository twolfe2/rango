from django.http import HttpResponse
from django.shortcuts import render

def index(request):
		context_dict = {'boldmessage':'I am a bold font from the context'}

		return render(request, 'rango/index.html', context_dict)