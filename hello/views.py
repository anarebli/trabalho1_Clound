from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, mundo!! A página de Django, da Ana Rebli, para a matéria de Computação em Núvem, está rodando!!")
    