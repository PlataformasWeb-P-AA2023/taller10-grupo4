from django.urls import path
from .views import listar, Parroquia_form, Barrio_form, Barrio_edit, Parroquias_edit, verbarrios, save_barrio

urlpatterns = [
    path('', listar, name="listar"),
    path('parroquia/', Parroquia_form, name="crearparroquia"),
    path('barrio/<int:id>', Barrio_form, name="crearbarrio"),
    path('barrio_edit/<int:id>', Barrio_edit, name="editarbarrio"),
    path('parroquia_edit/<int:id>', Parroquias_edit, name="editarparroquia"),
    path('verbarrios/<int:id>', verbarrios, name="verbarrios"),
    path('save/', save_barrio, name="save"),
]
