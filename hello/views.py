from django.http import HttpResponse, render

def home(request):
    return HttpResponse("Olá, mundo!! <br> A página de Django, da <b>Ana Rebli</b>, para a matéria de Computação em Núvem, está rodando!!")
    #return render(request, 'index.html')