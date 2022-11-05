from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import cliente, categoria, proveedor, tipoprenda,sastreria,establecimiento,nuevoListado,prendas,compra, producto, venta

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
    labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',        
    }



class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class categoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'

class proveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor 
        fields = '__all__'

class tipoprendaForm(forms.ModelForm):
    class Meta:
        model = tipoprenda
        fields = '__all__'

class sastreriaForm(forms.ModelForm):
    class Meta:
        model = sastreria
        fields = '__all__'

class establecimientoForm(forms.ModelForm):
    class Meta:
        model = establecimiento
        fields = '__all__'

class nuevolistadoForm(forms.ModelForm):
    class Meta:
        model = nuevoListado
        fields = '__all__'

class prendasForm(forms.ModelForm):
    class Meta:
        model = prendas
        fields = '__all__'

class comprasForm(forms.ModelForm):
    class Meta:
        model = compra
        fields = '__all__'

class productoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

class ventaForm(forms.ModelForm):
    class Meta:
        model = venta
        fields = '__all__'
