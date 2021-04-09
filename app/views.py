from django.shortcuts import render, redirect 
from django.http import HttpResponse
from app.forms import CarrosForm
from app.models import Carros

# Teste para ver se a aplicação esta funcionando de maneira correta 
# Create your views here.
# def home(request):
#     return HttpResponse('Teste inicial aprovado, pode avançar no projeto')

# Inicio das views do projeto
def home(request):
    data={}
    search=request.GET.get('search')
    # data['db'] = Carros.objects.all()
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()    
    return render(request, 'index.html',data)

# def form(request):
#     return render(request, 'form.html')

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def servico(request):
    #data = {}
    #data['form'] = CarrosForm()
    return render(request, 'servico.html')
    # return HttpResponse('Teste inicial aprovado, pode avançar no projeto')

def balanco(request):
    #data = {}
    #data['form'] = CarrosForm()
    return render(request, 'balanco.html')
    # return HttpResponse('Teste inicial aprovado, pode avançar no projeto')


def create(request):
    form = CarrosForm(request.POST or None) #Dados vindos do formulário
    if form.is_valid(): # Se os dados forem validos
        form.save() # salvar no banco de dados
        return redirect('home')

def view(request, pk): #recebendo o PK lá da URL
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')