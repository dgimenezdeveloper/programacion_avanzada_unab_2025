from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Libro, Merchandising, Consulta, Perfil
from .forms import LibroForm, MerchandisingForm, ConsultaForm, RegistroForm
from .carrito import Carrito
from itertools import chain
import operator

# --- Mixins (Para reutilizar lógica de permisos) ---

class StaffRequiredMixin(UserPassesTestMixin):
    """Mixin para requerir que el usuario sea staff."""
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'perfil') and self.request.user.perfil.rol == 'staff'

# --- Vistas de Productos (CBV) ---

class IndexView(ListView):
    template_name = 'tienda/index.html'
    context_object_name = 'productos'

    def get_queryset(self):
        query = self.request.GET.get('buscar')
        libros = Libro.objects.all()
        merchandising = Merchandising.objects.all()
        
        if query:
            libros = libros.filter(titulo__icontains=query)
            merchandising = merchandising.filter(titulo__icontains=query)
        
        queryset_combinado = chain(libros, merchandising)
        queryset_ordenado = sorted(queryset_combinado, key=operator.attrgetter('creacion'), reverse=True)
        return queryset_ordenado

class ProductoListView(ListView):
    template_name = 'tienda/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        categoria = self.kwargs.get('categoria')
        if categoria == 'libros':
            self.model = Libro
            return Libro.objects.all()
        elif categoria == 'merchandising':
            self.model = Merchandising
            return Merchandising.objects.all()
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria_titulo'] = self.kwargs.get('categoria').replace('-', ' ').title()
        return context

class ProductoDetailView(DetailView):
    template_name = 'tienda/producto_detail.html'
    context_object_name = 'producto'

    def get_object(self, queryset=None):
        # Obtenemos la categoría y la pk de los argumentos de la URL
        categoria = self.kwargs.get('categoria')
        pk = self.kwargs.get('pk')

        # Buscamos en el modelo correcto basado en la categoría
        if categoria == 'libro':
            # get_object_or_404 es una forma más limpia de hacer try/except
            return get_object_or_404(Libro, pk=pk)
        elif categoria == 'merchandising':
            return get_object_or_404(Merchandising, pk=pk)
        
        # Si la categoría no es válida, puedes devolver un error 404
        # o manejarlo como prefieras.
        from django.http import Http404
        raise Http404("Categoría de producto no válida")

class ProductoCreateView(StaffRequiredMixin, CreateView):
    template_name = 'tienda/producto_form.html'
    success_url = reverse_lazy('tienda:index')

    def get_form_class(self):
        categoria = self.kwargs.get('categoria')
        return LibroForm if categoria == 'libro' else MerchandisingForm
    
    def form_valid(self, form):
        messages.success(self.request, 'Producto creado con éxito.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = "Crear Nuevo Producto"
        return context

class ProductoUpdateView(StaffRequiredMixin, UpdateView):
    template_name = 'tienda/producto_form.html'
    context_object_name = 'producto'
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        try: return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist: return get_object_or_404(Merchandising, pk=pk)

    def get_form_class(self):
        return LibroForm if isinstance(self.object, Libro) else MerchandisingForm

    def get_success_url(self):
        return reverse_lazy('tienda:producto_detail', kwargs={'categoria': self.object.categoria, 'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado con éxito.')
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = "Editar Producto"
        return context


class ProductoDeleteView(StaffRequiredMixin, DeleteView):
    template_name = 'tienda/producto_confirm_delete.html'
    success_url = reverse_lazy('tienda:index')
    context_object_name = 'producto'

    def get_object(self):
        pk = self.kwargs.get('pk')
        try: return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist: return get_object_or_404(Merchandising, pk=pk)

    def form_valid(self, form):
        messages.success(self.request, 'Producto eliminado con éxito.')
        return super().form_valid(form)

# --- Vistas de Autenticación y Consultas ---

class CustomLoginView(LoginView):
    template_name = 'tienda/login.html'
    def form_valid(self, form):
        messages.success(self.request, f"Bienvenido/a, {form.get_user().username}!")
        return super().form_valid(form)

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Cuenta creada para {user.username}! Has iniciado sesión.')
            return redirect('tienda:index')
    else:
        form = RegistroForm()
    return render(request, 'tienda/registro.html', {'form': form})

class ConsultaView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    template_name = 'tienda/consulta.html'
    success_url = reverse_lazy('tienda:index')

    def form_valid(self, form):
        messages.success(self.request, 'Tu consulta ha sido enviada. Te responderemos pronto.')
        return super().form_valid(form)

class ConsultaListView(StaffRequiredMixin, ListView):
    model = Consulta
    template_name = 'tienda/consulta_list.html'
    context_object_name = 'consultas'

# --- Vistas funcionales (FBV) para páginas estáticas y el carrito ---

def about_me_view(request):
    return render(request, 'tienda/about_me.html')

@login_required
def carrito_view(request):
    return render(request, 'tienda/carrito.html')

@login_required
def agregar_al_carrito(request, producto_id):
    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'cliente':
        messages.error(request, "Debes ser un cliente para agregar productos al carrito.")
        return redirect('tienda:index')
    carrito = Carrito(request)
    try: producto = Libro.objects.get(id=producto_id)
    except Libro.DoesNotExist: producto = get_object_or_404(Merchandising, id=producto_id)
    carrito.agregar(producto)
    return redirect('tienda:carrito')

@login_required
def restar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    try: producto = Libro.objects.get(id=producto_id)
    except Libro.DoesNotExist: producto = get_object_or_404(Merchandising, id=producto_id)
    carrito.restar(producto)
    return redirect('tienda:carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    messages.info(request, "El carrito ha sido vaciado.")
    return redirect('tienda:carrito')

# --- VISTA PARA NOVEDADES ---
class NovedadesListView(ListView):
    template_name = 'tienda/producto_list.html' # Reutilizamos la misma plantilla
    context_object_name = 'productos'
    
    def get_queryset(self):
        # Buscamos en ambos modelos los que están marcados como novedad
        libros_novedad = Libro.objects.filter(es_novedad=True)
        merch_novedad = Merchandising.objects.filter(es_novedad=True)
        
        # Combinamos y ordenamos los resultados
        queryset_combinado = chain(libros_novedad, merch_novedad)
        queryset_ordenado = sorted(
            queryset_combinado, 
            key=lambda instance: instance.creacion, 
            reverse=True
        )
        return queryset_ordenado
        
    def get_context_data(self, **kwargs):
        # Añadimos un título personalizado para la plantilla
        context = super().get_context_data(**kwargs)
        context['categoria_titulo'] = "Nuestras Novedades"
        return context