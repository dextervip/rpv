# Create your views here.
from django.http import HttpResponse

def home(request):
    
    return HttpResponse('Ola, este e um teste do django... </br> Verificando se funciona...')