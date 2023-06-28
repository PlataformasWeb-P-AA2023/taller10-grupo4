from django.forms import ModelForm
from django import forms

from .models import Parroquia, Barrio


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


class BarrioParroquiaForm(ModelForm):

    def __init__(self, parroquia, *args, **kwargs):
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        self.initial['parroquia'] = parroquia
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)

    class Meta:
        model = Barrio
        fields = "__all__"

        """
        grupo4
        1234
        """


class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = '__all__'
