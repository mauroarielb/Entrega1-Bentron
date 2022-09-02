from django import forms

class AutosFormulario(forms.Form):
    
    marca=forms.CharField(max_length=50)
    anio_salida=forms.IntegerField()
    color=forms.CharField(max_length=50)




class MotosFormulario(forms.Form):
    
    marca=forms.CharField(max_length=50)
    anio_salida=forms.IntegerField()
    color=forms.CharField(max_length=50)


class BiciFormulario(forms.Form):
    
    marca=forms.CharField(max_length=50)
    anio_salida=forms.IntegerField()
    color=forms.CharField(max_length=50)
