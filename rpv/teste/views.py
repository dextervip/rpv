# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse('Olá, este é um teste do django')