from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- MODELO BASE ABSTRACTO ---
class Producto(models.Model):
    """ Modelo base abstracto para productos de la tienda.
        Contiene campos comunes a todos los productos como título, precio, imagen, categoría, descripción,
        fecha de creación y si es novedad.
        Los modelos concretos como Libro y Merchandising heredarán de este modelo."""
    CATEGORIA_CHOICES = (
        ('libro', 'Libro'),
        ('merchandising', 'Merchandising'),
    )
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, editable=False)
    texto = models.TextField(verbose_name="Descripción", null=True, blank=True)
    creacion = models.DateField(auto_now_add=True, null=True, blank=True)
    es_novedad = models.BooleanField(default=False, verbose_name="¿Es novedad?")
    
    creacion = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo

# --- MODELOS CONCRETOS QUE HEREDAN DE PRODUCTO ---
class Libro(Producto):
    """ Modelo concreto para libros que hereda de Producto.
        Añade un campo específico para el autor del libro."""
    autor = models.CharField(max_length=100, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        """ Sobrescribe el método save para establecer la categoría como 'libro' al guardar."""
        self.categoria = 'libro'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

class Merchandising(Producto):
    """ Modelo concreto para merchandising que hereda de Producto."""
    def save(self, *args, **kwargs):
        """ Sobrescribe el método save para establecer la categoría como 'merchandising' al guardar."""
        self.categoria = 'merchandising'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Merchandising"
        verbose_name_plural = "Merchandising"

# --- MODELO PARA CONSULTAS ---
class Consulta(models.Model):
    """ Modelo para almacenar consultas de los usuarios.
        Contiene campos para el nombre del usuario, email, consulta y fecha."""
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    consulta = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return f'Consulta de {self.nombre} el {self.fecha.strftime("%d/%m/%Y")}'

# --- MODELO ÚNICO DE PERFIL DE USUARIO ---
class Perfil(models.Model):
    """ Modelo para almacenar el perfil de usuario.
        Contiene un campo de relación uno a uno con User y un campo para el rol del usuario (cliente o staff)."""
    ROL_CHOICES = (('cliente', 'Cliente'), ('staff', 'Staff'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='cliente')

    def __str__(self):
        return f'Perfil de {self.user.username} ({self.get_rol_display()})'

# Signal para crear un Perfil automáticamente cuando se crea un User
@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfil.save()