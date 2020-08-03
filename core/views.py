from django.shortcuts import render, redirect
from core.models import Evento



# Create your views here.
def index(request):
    return redirect('/agenda/')
def lista_evento(request):
    usuario = request.user
    evento = Evento.objects.all()#filter(usuario=usuario)#cuidar com o .all devido a qt de registros
    dados = {'evento': evento}
    return render(request, 'agenda.html', dados)
