from django.db import models

# Create your models here.

class RubroComercio (models.Model): 
    nombre = models.TextField(default='')
    def __str__ (self):
        return self.nombre 

class Categoria (models.Model): 
    descripcion = models.TextField(default='')
    #flag = models.TextField(default='')
    def __str__ (self):
        return self.descripcion 

class Caracteristica (models.Model): 
    nombre = models.TextField(default='')
    def __str__ (self):
        return self.nombre 

class UnidadDeMedida (models.Model): 
    nombre = models.TextField(default='')
    def __str__ (self):
        return self.nombre 

class TipoCodigo (models.Model): 
    nombre = models.TextField(default='')
    def __str__ (self):
        return self.nombre 

class CaracteristicaProducto (models.Model):
    valor = models.TextField(default='')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    def __str__ (self):
        return "Característica %s: %s de %s" % (self.caracteristica, self.valor, self.producto)
    
class CodigoProducto (models.Model):    
    valor = models.TextField(default='')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    codigo = models.ForeignKey(TipoCodigo, on_delete=models.CASCADE)
    def __str__ (self):
        return "Codigo %s: %s de %s" % (self.codigo, self.valor, self.producto)
    
class MedidaProducto (models.Model): 
    valor = models.FloatField(default='')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadDeMedida, on_delete=models.CASCADE)
    def __str__ (self):
        return "%f %s(s) de %s" % (self.valor, self.unidad, self.producto)

class Comercio (models.Model): 
    nombre  = models.TextField(default='')
    rubro = models.ForeignKey(RubroComercio, on_delete=models.CASCADE)
    def __str__ (self):
        return self.nombre

class Producto (models.Model): 
    nombre = models.TextField(default='')
    comentario = models.TextField(default='')
    categorias = models.ManyToManyField(Categoria, blank=True)
    comercios = models.ManyToManyField(Comercio, blank=True)
    caracteristicas = models.ManyToManyField(Caracteristica, through='CaracteristicaProducto',blank=True)
    codigos = models.ManyToManyField(TipoCodigo, through='CodigoProducto', blank=True)
    medidas = models.ManyToManyField(UnidadDeMedida, through='MedidaProducto', blank=True)
    def __str__ (self):
        return self.nombre 




#-----------------------------------------------------------------------------------------------------
#PRUEBA CARGA MASIVA
#-----------------------------------------------------------------------------------------------------

#class Person(models.Model):
#    name = models.CharField(max_length=30)
#    email = models.EmailField(blank=True)
#    birth_date = models.DateField()
#    location = models.CharField(max_length=100, blank=True)

#ARMAR CARGA MASIVA PARA NO TENGO 