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


class SalesCheck(models.Model):
    totalToPay = models.BigIntegerField(verbose_name="Total a pagar")
    date = models.DateTimeField(verbose_name="Fecha de venta", auto_now_add="true")

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"


class Line(models.Model):
    product = models.CharField(max_length=64, verbose_name="Nombre")
    value = models.BigIntegerField(verbose_name="Valor", default=0)
    cuantity = models.IntegerField(verbose_name="Cantidad")
    totalValue = models.BigIntegerField(verbose_name="Valor total")
    salesCheck = models.ForeignKey(SalesCheck, related_name="lines", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
