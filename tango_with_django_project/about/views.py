from django.http import HttpResponse
from django.shortcuts import render

def index(request):
		context_dict = {'boldmessage':'I am a bold font from the context for the about page'}

		return render(request, 'rango/about.html', context_dict)