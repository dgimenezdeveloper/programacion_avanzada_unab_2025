from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from tienda import views

app_name = 'tienda'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Vistas principales
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.about_me_view, name='about_me'),
    
    # Autenticación y Usuarios
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),

    # Path para novedades
    path('novedades/', views.NovedadesListView.as_view(), name='novedades_list'),
    
    # Productos (Rutas unificadas)
    path('productos/<str:categoria>/', views.ProductoListView.as_view(), name='producto_list'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    
    # Gestión de Productos (Staff)
    path('producto/crear/<str:categoria>/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('producto/editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='producto_delete'),
    
    # Consultas
    path('consulta/', views.ConsultaView.as_view(), name='consulta_crear'),
    path('consultas/listado', views.ConsultaListView.as_view(), name='consulta_list'),
    
    # Carrito de Compras
    path('carrito/', views.carrito_view, name='carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='carrito_agregar'),
    path('carrito/restar/<int:producto_id>/', views.restar_del_carrito, name='carrito_restar'),
    path('carrito/limpiar/', views.limpiar_carrito, name='carrito_limpiar'),
]