from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia, Barrio

        


class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = '__all__'

"""

class NumeroTelefonicoForm(ModelForm):
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']




    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']
"""

class BarrioForm(ModelForm):
    class Meta:
        model =  Barrio
        fields = '__all__'



        
    
        """
        grupo4
        1234
        """