from django import forms

class Presupcorrform(forms.Form):
    nombre= forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=30)
    apellido= forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu apellido'}), min_length=3, max_length=30)
    telefono= forms.IntegerField(label="Telefono", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Telefono'}
    ))
    mail= forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    pedido= forms.CharField(label="Pedido", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Pedido a presupuestar'}
    ), min_length=3, max_length=1000)
    

