from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, mundo!! A página de Django, da Ana Rebli, está rodando!!")