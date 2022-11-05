from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from Apps.home.forms import RegistroForm, clienteForm, comprasForm, establecimientoForm, productoForm,proveedorForm,sastreriaForm,ventaForm, categoriaForm,tipoprendaForm,nuevolistadoForm, prendasForm



from Apps.home.models import cliente, compra, establecimiento, producto, proveedor, sastreria, venta, categoria, tipoprenda, nuevoListado, prendas
# Create your views here.

class Homeview(TemplateView):
    template_name='index.html'

class errorview(TemplateView):
    template_name='404.html'

class paginaBlank(TemplateView):
    template_name='blank.html'

class buttonsview(TemplateView):
    template_name='buttons.html'

class cardsview(TemplateView):
    template_name = 'cards.html'

class chartsview(TemplateView):
    template_name = 'charts.html'

class forgotview(TemplateView):
    template_name = 'forgot-password.html'

class loginview(TemplateView):
    template_name = 'login.html'

class registerview(TemplateView):
    template_name = 'register.html'

class tablesview(TemplateView):
    template_name = 'tables.html'

class utilitiesanimationview(TemplateView):
    template_name = 'utilities-animation.html'

class utilitiesborder(TemplateView):
    template_name = 'utilities-border.html'

class utilitiescolor(TemplateView):
    template_name = 'utilities-color.html'

class utilitiesother(TemplateView):
    template_name = 'utilities-other.html'


class categorias(ListView):
    template_name = '8categoria.html'
    model = categoria
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return categoria.objects.filter(nombre__icontains=vNombres)
        else:
            return categoria.objects.all()

class tipoprendas(ListView):
    template_name = '9tipoprenda.html'
    model = tipoprenda
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return tipoprenda.objects.filter(nombre__icontains=vNombres)
        else:
            return tipoprenda.objects.all()

class nuevoListados(ListView):
    template_name = '10nuevoListado.html'
    model = nuevoListado
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return nuevoListado.objects.filter(nombre__icontains=vNombres)
        else:
            return nuevoListado.objects.all()

class prenda(ListView):
    template_name = '11prendas.html'
    model = prendas
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return prendas.objects.filter(nombre__icontains=vNombres)
        else:
            return prendas.objects.all()

class productos(ListView):
    template_name = '1productos.html'
    model = producto
    paginate_by = 3
    def get_queryset(self):
        vNombre = self.request.GET.get('nombre')
        if(vNombre):
            return producto.objects.filter(nombre__icontains=vNombre)
        else:
            return producto.objects.all()

class compras(ListView):
    template_name = '2compra.html'
    model = compra
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('cantidad')
        if(vNombres):
            return compra.objects.filter(cantidad__icontains=vNombres)
        else:
            return compra.objects.all()

class ventas(ListView):
    template_name = '3venta.html'
    model = venta
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('cantidad')
        if(vNombres):
            return venta.objects.filter(cantidad__icontains=vNombres)
        else:
            return venta.objects.all()

class proveedores(ListView):
    template_name = '4proveedores.html'
    model = proveedor
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('cantidad')
        if(vNombres):
            return proveedor.objects.filter(cantidad__icontains=vNombres)
        else:
            return proveedor.objects.all()

class clientes(ListView):
    template_name = '5clientes.html'
    model = cliente
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return cliente.objects.filter(nombre__icontains=vNombres)
        else:
            return cliente.objects.all()


class establecimientos(ListView):
    template_name = '6establecimiento.html'
    model = establecimiento
    paginate_by = 3
    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return establecimiento.objects.filter(nombre__icontains=vNombres)
        else:
            return establecimiento.objects.all()


class sastrerias(ListView):
    template_name = '7sastreria.html'
    model = sastreria
    paginate_by = 3


    def get_queryset(self):
        vNombres = self.request.GET.get('nombre')
        if(vNombres):
            return sastreria.objects.filter(nombre__icontains=vNombres)
        else:
            return sastreria.objects.all()

class verProducto(ListView):
    template_name = 'jproductos.html'
    model= compra, producto


    def get_query(self):
        return compra.objects.all(), producto.objects.all()

class RegistroUsuario(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home:index')

class insertarCliente(CreateView):
    model = cliente
    template_name= 'icliente.html'
    form_class = clienteForm
    success_url = reverse_lazy('home:clientes')

class insertarCategoria(CreateView):
    model = categoria
    template_name= 'icategoria.html'
    form_class = categoriaForm
    success_url = reverse_lazy('home:categorias')

class insertarProveedor(CreateView):
    model = proveedor
    template_name= 'iproveedor.html'
    form_class = proveedorForm
    success_url = reverse_lazy('home:proveedores')

class insertartipoPrenda(CreateView):
    model = tipoprenda
    template_name= 'itipoprenda.html'
    form_class = tipoprendaForm
    success_url = reverse_lazy('home:tipoprendas')

class insertarSastreria(CreateView):
    model = sastreria
    template_name= 'isastreria.html'
    form_class = sastreriaForm
    success_url = reverse_lazy('home:sastrerias')

class insertarEstablecimiento(CreateView):
    model = establecimiento
    template_name= 'iestablecimiento.html'
    form_class = establecimientoForm
    success_url = reverse_lazy('home:establecimientos')

class insertarnuevoListado(CreateView):
    model = nuevoListado
    template_name= 'inuevoListado.html'
    form_class = nuevolistadoForm
    success_url = reverse_lazy('home:nuevoListado')

class insertarPrenda(CreateView):
    model = prendas
    template_name= 'iprendas.html'
    form_class = prendasForm
    success_url = reverse_lazy('home:prendas')

class insertarCompra(CreateView):
    model = compra
    template_name= 'icompras.html'
    form_class = comprasForm
    success_url = reverse_lazy('home:compras')

class insertarProducto(CreateView):
    model = producto
    template_name= 'iproductos.html'
    form_class = productoForm
    success_url = reverse_lazy('home:productos')

class insertarVenta(CreateView):
    model = venta
    template_name= 'iventa.html'
    form_class = ventaForm
    success_url = reverse_lazy('home:ventas')














class EditarCliente(UpdateView):
    model = cliente
    template_name= 'icliente.html'
    form_class = clienteForm
    success_url = reverse_lazy('home:clientes')

class EditarCategoria(UpdateView):
    model = categoria
    template_name= 'icategoria.html'
    form_class = categoriaForm
    success_url = reverse_lazy('home:categorias')

class EditarProveedor(UpdateView):
    model = proveedor
    template_name= 'iproveedor.html'
    form_class = proveedorForm
    success_url = reverse_lazy('home:proveedores')

class EditartipoPrenda(UpdateView):
    model = tipoprenda
    template_name= 'itipoprenda.html'
    form_class = tipoprendaForm
    success_url = reverse_lazy('home:tipoprendas')

class EditarSastreria(UpdateView):
    model = sastreria
    template_name= 'isastreria.html'
    form_class = sastreriaForm
    success_url = reverse_lazy('home:sastrerias')

class EditarEstablecimiento(UpdateView):
    model = establecimiento
    template_name= 'iestablecimiento.html'
    form_class = establecimientoForm
    success_url = reverse_lazy('home:establecimientos')

class EditarnuevoListado(UpdateView):
    model = nuevoListado
    template_name= 'inuevoListado.html'
    form_class = nuevolistadoForm
    success_url = reverse_lazy('home:nuevoListado')

class EditarPrenda(UpdateView):
    model = prendas
    template_name= 'iprendas.html'
    form_class = prendasForm
    success_url = reverse_lazy('home:prendas')

class EditarCompra(UpdateView):
    model = compra
    template_name= 'icompras.html'
    form_class = comprasForm
    success_url = reverse_lazy('home:compras')

class EditarProducto(UpdateView):
    model = producto
    template_name= 'iproductos.html'
    form_class = productoForm
    success_url = reverse_lazy('home:productos')

class EditarVenta(UpdateView):
    model = venta
    template_name= 'iventa.html'
    form_class = ventaForm
    success_url = reverse_lazy('home:ventas')


