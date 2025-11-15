from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.db import transaction
from django.db.models import Sum
from django.db.models.functions import TruncDate
import json

from .models import Venta
from .forms import VentaForm, ItemVentaFormSet



class VentaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Venta
    template_name = 'ventas/lista.html'
    context_object_name = 'ventas'
    permission_required = "ventas.view_venta"



class VentaDetalleView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Venta
    template_name = 'ventas/detalle.html'
    context_object_name = 'venta'
    permission_required = "ventas.view_venta"



class VentaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Venta
    template_name = 'ventas/confirmar_borrado.html'
    success_url = reverse_lazy('ventas_lista')
    permission_required = "ventas.delete_venta"


class VentasPorDiaView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'ventas/grafico_ventas.html'
    permission_required = "ventas.view_venta"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ventas_por_dia = (
            Venta.objects
            .annotate(fecha_dia=TruncDate('fecha'))
            .values('fecha_dia')
            .annotate(total_dia=Sum('total'))
            .order_by('fecha_dia')
        )

        labels = [v['fecha_dia'].strftime('%Y-%m-%d') for v in ventas_por_dia]
        data = [float(v['total_dia']) for v in ventas_por_dia]

        context['labels'] = json.dumps(labels)
        context['data'] = json.dumps(data)
        return context


@login_required
@permission_required('ventas.add_venta', raise_exception=True)
@transaction.atomic
def nueva_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        formset = ItemVentaFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            # Validar que hay al menos un item
            items_validos = [item for item in formset if item.cleaned_data and not item.cleaned_data.get('DELETE', False)]
            
            if not items_validos:
                messages.error(request, "Debe agregar al menos un producto a la venta.")
                return render(request, 'ventas/form.html', {'form': form, 'formset': formset})
            
            venta = form.save(commit=False)
            venta.total = 0
            venta.save()

            for item_form in items_validos:
                item = item_form.save(commit=False)
                item.venta = venta
                item.precio_unitario = item.precio_unitario or item.producto.precio
                item.subtotal = item.cantidad * item.precio_unitario
                item.save()
                venta.total += item.subtotal

            venta.save()
            messages.success(request, "Venta registrada correctamente.")
            return redirect('ventas_lista')
    else:
        form = VentaForm()
        formset = ItemVentaFormSet()

    return render(request, 'ventas/form.html', {'form': form, 'formset': formset})
