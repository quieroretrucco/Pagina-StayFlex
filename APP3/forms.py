from django import forms
 
class DepartamentoFormulario(forms.Form):
    barrio=forms.CharField(max_length=40)
    piso=forms.IntegerField()
    depto=forms.CharField(max_length=40)

class PropietarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
   
class HuespedFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    nacionalidad = forms.CharField(max_length=30)
   
class EstadiaFormulario(forms.Form):
    check_in = forms.DateField()
    check_out = forms.DateField()