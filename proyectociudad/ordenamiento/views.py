from django.shortcuts import render, redirect
from traitlets import link

from .models import Parroquia, Barrio
from .forms import BarrioForm, ParroquiaForm, BarrioParroquiaForm


# Create your views here.
def listar(request):
    return render(request, 'listar.html', {'data': Parroquia.objects.all()})


def Parroquia_form(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar)
    else:
        form = ParroquiaForm()
    return render(request, 'parroquia_form.html', {'form': form})


def save_barrio(request):
    form = BarrioForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(listar)


def Barrio_form(request, id):
    p = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioParroquiaForm(p, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar)
    else:
        formulario = BarrioParroquiaForm(p)
    # diccionario = {'formulario': formulario, 'estudiante': estudiante}
    return render(request, 'barrio_form.html', {"form": formulario})


def Parroquias_edit(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        form = ParroquiaForm(request.POST, instance=parroquia)
        if form.is_valid():
            form.save()
            return redirect(listar)
    else:
        form = ParroquiaForm(instance=parroquia)
    return render(request, 'parroquia_form.html', {'form': form})


def Barrio_edit(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        form = BarrioForm(request.POST, instance=barrio)
        if form.is_valid():
            form.save()

            return redirect(listar)
    else:
        form = BarrioForm(instance=barrio)

    return render(request, 'barrio_form.html', {'form': form})


def verbarrios(request, id):
    return render(request, 'verbarrios.html', {'data': Parroquia.objects.get(pk=id)})
