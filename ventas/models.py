import uuid
from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from productos.models import Producto

def generar_codigo():
    return str(uuid.uuid4())

class Venta(models.Model):
    codigo = models.CharField(max_length=36, unique=True, default=generar_codigo)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.codigo} - {self.cliente}"

    def calcular_total(self):
        total = sum(item.subtotal for item in self.items.all())
        self.total = total
        self.save(update_fields=["total"])
        return total


class ItemVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        creando = self._state.adding
        self.precio_unitario = self.precio_unitario or self.producto.precio
        self.subtotal = self.cantidad * self.precio_unitario

        # verificar el stock
        if creando and self.producto.stock < self.cantidad:
            raise ValueError(f"Stock insuficiente para {self.producto.nombre}")

        super().save(*args, **kwargs)

        if creando:
            self.producto.stock -= self.cantidad
            self.producto.save()
            self.venta.calcular_total()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"


