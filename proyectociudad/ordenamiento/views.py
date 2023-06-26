from django.shortcuts import render,redirect
from .models import Parroquia,Barrio
from .forms import BarrioForm,ParroquiaForm

# Create your views here.
def listar(request):
    return render(request, 'listar.html',{ 'data':Parroquia.objects.all()})

def Parroquia_form(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar)
    else:
        form = ParroquiaForm()
    return render(request, 'parroquia_form.html', {'form': form})

def Barrio_form(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar)
    else:
        form = BarrioForm()
    return render(request, 'barrio_form.html', {'form': form})


def Parroquias_edit(request,id):
    parroquia= Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        form = ParroquiaForm(request.POST,instance= parroquia)
        if form.is_valid():
            form.save()
            return redirect(listar)
    else:
        form = ParroquiaForm(instance=parroquia)
    return render(request, 'parroquia_form.html', {'form': form})


def Barrio_edit(request,id):
    barrio=Barrio.objects.get(pk=id)
    if request.method == 'POST':
        form = BarrioForm(request.POST,instance=barrio)
        if form.is_valid():
            form.save()
            
            return redirect(listar)
    else:
        form = BarrioForm(instance=barrio)
        
    return render(request, 'barrio_form.html', {'form': form})
def verbarrios(request , id):
    return render(request, 'verbarrios.html',{ 'data':Parroquia.objects.get(pk=id) })



