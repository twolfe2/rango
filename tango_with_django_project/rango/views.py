from django.http import HttpResponse

def index(request):
		return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")