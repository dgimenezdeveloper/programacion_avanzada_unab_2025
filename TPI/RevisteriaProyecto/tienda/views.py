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
    """ Vista para la página de inicio que muestra productos de ambos tipos (libros y merchandising)."""
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
    """ Vista para listar productos de una categoría específica (libros o merchandising).
        La categoría se determina a partir de la URL."""
    template_name = 'tienda/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        """ Devuelve los productos de la categoría especificada en la URL."""
        categoria = self.kwargs.get('categoria')
        if categoria == 'libros':
            self.model = Libro
            return Libro.objects.all()
        elif categoria == 'merchandising':
            self.model = Merchandising
            return Merchandising.objects.all()
        return []

    def get_context_data(self, **kwargs):
        """ Añade un título personalizado al contexto para la plantilla."""
        context = super().get_context_data(**kwargs)
        context['categoria_titulo'] = self.kwargs.get('categoria').replace('-', ' ').title()
        return context

class ProductoDetailView(DetailView):
    """ Vista para mostrar los detalles de un producto específico.
        La categoría y la pk del producto se obtienen de los argumentos de la URL."""
    template_name = 'tienda/producto_detail.html'
    context_object_name = 'producto'

    def get_object(self, queryset=None):
        # Obtiene la categoría y la pk de los argumentos de la URL
        categoria = self.kwargs.get('categoria')
        pk = self.kwargs.get('pk')

        # Busca en el modelo correcto basado en la categoría
        if categoria == 'libro':
            return get_object_or_404(Libro, pk=pk)
        elif categoria == 'merchandising':
            return get_object_or_404(Merchandising, pk=pk)
        
        from django.http import Http404
        raise Http404("Categoría de producto no válida")

class ProductoCreateView(StaffRequiredMixin, CreateView):
    """ Vista para crear un nuevo producto.
        La categoría del producto se determina a partir de los argumentos de la URL."""
    template_name = 'tienda/producto_form.html'
    success_url = reverse_lazy('tienda:index')

    def get_form_class(self):
        """ Devuelve el formulario adecuado según la categoría del producto."""
        categoria = self.kwargs.get('categoria')
        return LibroForm if categoria == 'libro' else MerchandisingForm
    
    def form_valid(self, form):
        """ Procesa el formulario y muestra un mensaje de éxito."""
        messages.success(self.request, 'Producto creado con éxito.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        """ Añade un título personalizado al contexto para la plantilla."""
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = "Crear Nuevo Producto"
        return context

class ProductoUpdateView(StaffRequiredMixin, UpdateView):
    """ Vista para editar un producto existente.
        La categoría del producto se determina a partir de la pk del objeto."""
    template_name = 'tienda/producto_form.html'
    context_object_name = 'producto'
    
    def get_object(self):
        """ Obtiene el objeto a editar, buscando primero en Libro y luego en Merchandising."""
        pk = self.kwargs.get('pk')
        try: return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist: return get_object_or_404(Merchandising, pk=pk)

    def get_form_class(self):
        """ Devuelve el formulario adecuado según el tipo de producto."""
        return LibroForm if isinstance(self.object, Libro) else MerchandisingForm

    def get_success_url(self):
        """ Redirige a la página de detalles del producto editado."""
        return reverse_lazy('tienda:producto_detail', kwargs={'categoria': self.object.categoria, 'pk': self.object.pk})

    def form_valid(self, form):
        """ Procesa el formulario y muestra un mensaje de éxito."""
        messages.success(self.request, 'Producto actualizado con éxito.')
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        """ Añade un título personalizado al contexto para la plantilla."""
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = "Editar Producto"
        return context


class ProductoDeleteView(StaffRequiredMixin, DeleteView):
    """ Vista para eliminar un producto existente.
        La categoría del producto se determina a partir de la pk del objeto."""
    template_name = 'tienda/producto_confirm_delete.html'
    success_url = reverse_lazy('tienda:index')
    context_object_name = 'producto'

    def get_object(self):
        """ Obtiene el objeto a eliminar, buscando primero en Libro y luego en Merchandising."""
        pk = self.kwargs.get('pk')
        try: return Libro.objects.get(pk=pk)
        except Libro.DoesNotExist: return get_object_or_404(Merchandising, pk=pk)

    def form_valid(self, form):
        """ Procesa la eliminación del producto y muestra un mensaje de éxito."""
        messages.success(self.request, 'Producto eliminado con éxito.')
        return super().form_valid(form)

# --- Vistas de Autenticación y Consultas ---

class CustomLoginView(LoginView):
    """ Vista personalizada para el inicio de sesión de usuarios. """
    template_name = 'tienda/login.html'
    def form_valid(self, form):
        messages.success(self.request, f"Bienvenido/a, {form.get_user().username}!")
        return super().form_valid(form)

def registro_view(request):
    """ Vista para el registro de nuevos usuarios.
        Utiliza un formulario personalizado para crear un nuevo usuario y su perfil."""
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
    """ Vista para crear una nueva consulta.
        Utiliza un formulario personalizado para recoger la consulta del usuario."""
    model = Consulta
    form_class = ConsultaForm
    template_name = 'tienda/consulta.html'
    success_url = reverse_lazy('tienda:index')

    def form_valid(self, form):
        messages.success(self.request, 'Tu consulta ha sido enviada. Te responderemos pronto.')
        return super().form_valid(form)

class ConsultaListView(StaffRequiredMixin, ListView):
    """ Vista para listar todas las consultas enviadas por los usuarios.
        Requiere que el usuario sea staff para acceder."""
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
    """ Vista para agregar un producto al carrito.
        Requiere que el usuario sea cliente y que el producto exista."""
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
    """ Vista para restar un producto del carrito.
        Requiere que el usuario sea cliente y que el producto exista."""
    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'cliente':
        messages.error(request, "Debes ser un cliente para restar productos del carrito.")
        return redirect('tienda:index')
    carrito = Carrito(request)
    try: producto = Libro.objects.get(id=producto_id)
    except Libro.DoesNotExist: producto = get_object_or_404(Merchandising, id=producto_id)
    carrito.restar(producto)
    return redirect('tienda:carrito')

@login_required
def limpiar_carrito(request):
    """ Vista para limpiar el carrito de compras.
        Requiere que el usuario sea cliente."""
    if not hasattr(request.user, 'perfil') or request.user.perfil.rol != 'cliente':
        messages.error(request, "Debes ser un cliente para limpiar el carrito.")
        return redirect('tienda:index')
    # Limpiamos el carrito
    carrito = Carrito(request)
    carrito.limpiar()
    messages.info(request, "El carrito ha sido vaciado.")
    return redirect('tienda:carrito')

# --- VISTA PARA NOVEDADES ---
class NovedadesListView(ListView):
    """ Vista para listar productos que están marcados como novedades.
        Combina libros y merchandising en una sola lista."""
    template_name = 'tienda/producto_list.html' # Reutilizamos la misma plantilla
    context_object_name = 'productos'
    
    def get_queryset(self):
        """ Devuelve los productos que están marcados como novedades.
            Combina libros y merchandising en una sola lista ordenada por fecha de creación."""
        libros_novedad = Libro.objects.filter(es_novedad=True)
        merch_novedad = Merchandising.objects.filter(es_novedad=True)
        
        queryset_combinado = chain(libros_novedad, merch_novedad)
        queryset_ordenado = sorted(
            queryset_combinado, 
            key=lambda instance: instance.creacion, 
            reverse=True
        )
        return queryset_ordenado
        
    def get_context_data(self, **kwargs):
        """ Añade un título personalizado al contexto para la plantilla."""
        context = super().get_context_data(**kwargs)
        context['categoria_titulo'] = "Nuestras Novedades"
        return context