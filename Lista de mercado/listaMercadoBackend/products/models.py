from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nombre")
    value = models.BigIntegerField(verbose_name="Valor")
    description = models.TextField(verbose_name="Descripción")
    stock = models.IntegerField(verbose_name="Existencia")
    available = models.BooleanField(verbose_name="Disponible")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class ProductXLine(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nombre")
    value = models.BigIntegerField(verbose_name="Valor")


class Line(models.Model):
    totalValue = models.BigIntegerField(verbose_name="Valor total")
    product = models.ForeignKey(ProductXLine, verbose_name="Producto", related_name="get_product",
                                on_delete=models.PROTECT)
    cuantity = models.IntegerField(verbose_name="Cantidad")


class SalesCheck(models.Model):
    totalToPay = models.BigIntegerField(verbose_name="Total a pagar")
    lines = models.ManyToManyField(Line, verbose_name="Linea")
    date = models.DateTimeField(verbose_name="Fecha de venta", auto_now_add="true")

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
