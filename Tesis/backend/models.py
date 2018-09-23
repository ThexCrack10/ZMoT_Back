from django.db import models

# Create your models here.

class RubroComercio (models.Model): 
    pass

class Categoria (models.Model): 
    pass

class Caracteristica (models.Model): 
    pass

class UnidadDeMedida (models.Model): 
    pass

class TipoCodigo (models.Model): 
    pass

class CaracteristicaProducto (models.Model): 
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    valor = models.TextField()

class CodigoProducto (models.Model):    
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    codigo = models.ForeignKey(TipoCodigo, on_delete=models.CASCADE)
    valor = models.TextField()

class MedidaProducto (models.Model): 
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadDeMedida, on_delete=models.CASCADE)
    valor = models.FloatField()

class Comercio (models.Model): 
    rubro = models.ForeignKey(RubroComercio, on_delete=models.CASCADE)

class Producto (models.Model): 
    categorias = models.ManyToManyField(Categoria)
    comercios = models.ManyToManyField(Comercio)
    caracteristicas = models.ManyToManyField(Caracteristica, through='CaracteristicaProducto')
    codigos = models.ManyToManyField(TipoCodigo, through='CodigoProducto')
    medidas = models.ManyToManyField(UnidadDeMedida, through='MedidaProducto')



