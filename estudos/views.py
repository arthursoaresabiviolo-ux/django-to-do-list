from django.shortcuts import render

def index_view(request):
    return render(request, 'estudos/home.html')

def tarefas_home(request):
    contexto = {
        'nome':'Arthur',
        'tarefas': TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', contexto)