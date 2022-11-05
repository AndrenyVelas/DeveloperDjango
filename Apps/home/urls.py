"""Tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from re import template
from django.contrib import admin
from django.urls import path, include
from Apps.home import views
from .views import Homeview, RegistroUsuario, buttonsview, cardsview, chartsview, clientes, errorview, establecimientos, forgotview, loginview, paginaBlank, productos, proveedores, registerview, sastrerias, tablesview, utilitiesanimationview, utilitiesborder, utilitiescolor, utilitiesother, compras, ventas, categorias, tipoprendas,nuevoListados, prenda, insertarCliente, insertarCategoria, insertarProveedor, insertartipoPrenda, insertarSastreria, insertarEstablecimiento, insertarnuevoListado, insertarPrenda, insertarCompra, insertarProducto, insertarVenta, EditarCategoria, EditarCliente, EditarCompra, EditarEstablecimiento, EditarnuevoListado, EditarPrenda, EditarProducto, EditarProveedor, EditarSastreria, EditartipoPrenda, EditarVenta, verProducto
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

app_name = 'home'

urlpatterns = [

    path('logout/', logout_then_login, name = 'logout'),
    path('index', login_required(Homeview.as_view()), name='index'),
    path('error/', login_required(errorview.as_view()), name = 'error'),
    path('black/', login_required(paginaBlank.as_view()), name='blackk'),
    path('buttons/', login_required(buttonsview.as_view()), name = 'buttonss'),
    path('cards/', login_required(cardsview.as_view()), name='cardss'),
    path('charts/', login_required(chartsview.as_view()), name = 'chartss'),
    path('register/',login_required(RegistroUsuario.as_view()), name='registerr'),
    path('tables/', login_required(tablesview.as_view()), name = 'tabless'),
    path('animation/', login_required(utilitiesanimationview.as_view()), name='animationn'),
    path('border/', login_required(utilitiesborder.as_view()), name = 'borderr'),
    path('color/', login_required(utilitiescolor.as_view()), name='colorr'),
    path('other/', login_required(utilitiesother.as_view()), name = 'otherr'),
    path('', login_required(productos.as_view()), name = 'productos'),
    path('compra/', login_required(compras.as_view()), name = 'compras'),
    path('venta/', login_required(ventas.as_view()), name = 'ventas'),
    path('proveedores/', login_required(proveedores.as_view()), name = 'proveedores'),
    path('clientes/', login_required(clientes.as_view()), name = 'clientes'),
    path('categorias/', login_required(categorias.as_view()), name = 'categorias'),
    path('nuevoListado/', login_required(nuevoListados.as_view()), name = 'nuevoListado'),
    path('tipoprendas/', login_required(tipoprendas.as_view()), name = 'tipoprendas'),
    path('prendas/', login_required(prenda.as_view()), name = 'prendas'),
    path('establecimientos/', login_required(establecimientos.as_view()), name = 'establecimientos'),
    path('sastrerias/', login_required(sastrerias.as_view()), name = 'sastrerias'),

    path('insertarCliente', login_required(insertarCliente.as_view()), name = 'insertcliente'),
    path('insertarCategoria', login_required(insertarCategoria.as_view()), name = 'insertcategoria'),
    path('insertarProveedor', login_required(insertarProveedor.as_view()), name = 'insertproveedor'),
    path('insertartipoPrenda', login_required(insertartipoPrenda.as_view()), name = 'insertprenda'),
    path('insertarSastreria', login_required(insertarSastreria.as_view()), name = 'insertSastreria'),
    path('insertarEstablecimiento', login_required(insertarEstablecimiento.as_view()), name = 'insertEstablecimiento'),
    path('insertarnuevoListado', login_required(insertarnuevoListado.as_view()), name = 'insertnuevoListado'),
    path('insertarPrenda', login_required(insertarPrenda.as_view()), name = 'insertPrenda'),
    path('insertarCompra', login_required(insertarCompra.as_view()), name = 'insertCompra'),
    path('insertarProducto', login_required(insertarProducto.as_view()), name = 'insertProducto'),
    path('insertarVenta', login_required(insertarVenta.as_view()), name = 'insertVenta'),
    



    path('EditarCliente/<int:pk>', login_required(EditarCliente.as_view()), name = 'editcliente'),
    path('EditarCategoria/<int:pk>', login_required(EditarCategoria.as_view()), name = 'editcategoria'),
    path('EditarProveedor/<int:pk>', login_required(EditarProveedor.as_view()), name = 'editproveedor'),
    path('EditartipoPrenda/<int:pk>', login_required(EditartipoPrenda.as_view()), name = 'editprenda'),
    path('EditarSastreria/<int:pk>', login_required(EditarSastreria.as_view()), name = 'editSastreria'),
    path('EditarEstablecimiento/<int:pk>', login_required(EditarEstablecimiento.as_view()), name = 'editEstablecimiento'),
    path('EditarnuevoListado/<int:pk>', login_required(EditarnuevoListado.as_view()), name = 'editnuevoListado'),
    path('EditarPrenda/<int:pk>', login_required(EditarPrenda.as_view()), name = 'editPrenda'),
    path('EditarCompra/<int:pk>', login_required(EditarCompra.as_view()), name = 'editCompra'),
    path('EditarProducto/<int:pk>', login_required(EditarProducto.as_view()), name = 'editProducto'),
    path('EditarVenta/<int:pk>', login_required(EditarVenta.as_view()), name = 'editVenta'),
    

    path('VerProductos/', login_required(verProducto.as_view()), name = 'ver'),  

]
