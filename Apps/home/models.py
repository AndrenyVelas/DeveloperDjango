from email.policy import default
from enum import _auto_null, auto
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User



class cliente(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=150, null=True, blank=True)
    direccion = models.CharField(max_length=150)
    nit = models.IntegerField()
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class categoria(models.Model):
    nombre = models.CharField(max_length=150)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=150)
    correo = models.CharField(max_length=150, null=True, blank=True)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class tipoprenda(models.Model):
    nombre = models.CharField(max_length=150)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class sastreria(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    tipoPrenda = models.ForeignKey(tipoprenda,on_delete=models.CASCADE)
    medidas = models.CharField(max_length=150)
    precio = models.IntegerField()
    anticipo = models.IntegerField()
    pendiente = models.IntegerField()
    realizado = models.CharField(max_length=2)
    entregado = models.CharField(max_length=2)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class establecimiento(models.Model):
    nombre = models.CharField(max_length=150)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class nuevoListado(models.Model):
    nombre = models.CharField(max_length=150)
    establecimiento = models.ForeignKey(establecimiento,on_delete=models.CASCADE)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class prendas(models.Model):
    listado= models.ForeignKey(nuevoListado,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    tipoPrenda= models.ForeignKey(tipoprenda,on_delete=models.CASCADE)
    medidas = models.CharField(max_length=150)
    precio = models.IntegerField()
    anticipo = models.IntegerField()
    pendiente = models.IntegerField()
    realizado = models.CharField(max_length=2)
    entregado = models.CharField(max_length=2)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class compra(models.Model):
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)

class producto(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=25)
    cantidad = models.IntegerField()
    precioCompra = models.IntegerField()
    precioVenta = models.IntegerField()
    categoria = models.ForeignKey(categoria,on_delete=models.CASCADE)
    proveedor = models.ForeignKey(proveedor,on_delete=models.CASCADE)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)






class venta(models.Model):
    producto = models.ManyToManyField(producto)
    precioUnidad = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    cliente = models.ForeignKey(cliente,on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    creacion = models.DateField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.nombre)
