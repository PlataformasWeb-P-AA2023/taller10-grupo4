from django.shortcuts import render
from .models import Parroquia,Barrio
# Create your views here.
def listar(request):
    return render(request, 'listar.html',{ 'data':Parroquia.objects.all()})


