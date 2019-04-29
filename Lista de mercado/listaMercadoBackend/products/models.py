from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nombre")
    value = models.BigIntegerField(verbose_name="Valor")
    description = models.TextField(verbose_name="Descripción")
    stock = models.IntegerField(verbose_name="Existencia")
    available = models.BooleanField(verbose_name="Disponible")

    def save(self, *args, **kwargs):
        try:
            if self.stock > 0:
                self.available = True
            else:
                self.available = False
        except Product.DoesNotExist:
            pass
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class SalesCheck(models.Model):
    totalToPay = models.BigIntegerField(verbose_name="Total a pagar")
    date = models.DateTimeField(verbose_name="Fecha de venta", auto_now_add="true")

    def save(self, *args, **kwargs):
        try:
            total = 0
            for line in self.lines:
                total += line.totalValue
            self.totalToPay = total
        except SalesCheck.DoesNotExist:
            pass
        super(SalesCheck, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        try:
            self.totalValue = self.value * self.cuantity
        except Line.DoesNotExist:
            pass
        super(Line, self).save(*args, **kwargs)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
