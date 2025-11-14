from django import forms
from django.forms import inlineformset_factory
from .models import Venta, ItemVenta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']

ItemVentaFormSet = inlineformset_factory(
    Venta,
    ItemVenta,
    fields=('producto', 'cantidad', 'precio_unitario', 'subtotal'),
    extra=1,
    can_delete=True
)
