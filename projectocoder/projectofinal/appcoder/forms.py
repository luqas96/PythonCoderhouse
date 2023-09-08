from django import forms


class CursoFormulario(forms.Form):

     curso = forms.CharField()
     camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
     nombre= forms.CharField()
     apellido= forms.CharField()
     mail= forms.EmailField()
     profesion= forms.CharField()


class EstudianteFormulario(forms.Form):
     nombre= forms.CharField()
     apellido= forms.CharField()
     mail= forms.EmailField()

class EntregableFormulario(forms.Form):
     nombre= forms.CharField(max_length=30)
     fecha_entrega= forms.DateField()
     entregado= forms.BooleanField()
