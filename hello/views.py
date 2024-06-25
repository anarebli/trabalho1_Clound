from django.http import HttpResponse, render

def home(request):
    #return HttpResponse("Olá, mundo!! <br> A página de Django, da Ana Rebli, está rodando!!")
    return render(request, 'index.html')