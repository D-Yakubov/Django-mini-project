from django.shortcuts import render
#from django.http import HttpResponse
from .models import Dictionary

def index(request):

	word = request.GET.get('q', "")
	if word and word != "":
		result = Dictionary.objects.filter(english__contains=word).all()[:3]
	else:
		result=None


	return render(request, 'index.html', {"q":word, "result": result})