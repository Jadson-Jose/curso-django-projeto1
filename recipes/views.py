from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, 'recipes/home.html', context={
      'name': 'Jadson',  
    })


def contato(requeste):
    return HttpResponse('contato')
