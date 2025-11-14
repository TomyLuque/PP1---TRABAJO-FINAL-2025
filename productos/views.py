from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Producto
from .forms import ProductoForm


class ProductoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Producto
    template_name = "productos/lista.html"
    context_object_name = "productos"
    paginate_by = 10
    permission_required = "productos.view_producto"

    def get_queryset(self):
        queryset = Producto.objects.all().order_by("nombre")

        nombre = self.request.GET.get("nombre", "")
        stock_bajo = self.request.GET.get("stock_bajo")

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        if stock_bajo == "1":
            queryset = queryset.filter(stock__lte=5)

        return queryset


class ProductoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/form.html"
    success_url = reverse_lazy("productos:lista")
    permission_required = "productos.add_producto"

    def form_valid(self, form):
        messages.success(self.request, "Producto creado correctamente.")
        return super().form_valid(form)


class ProductoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "productos/form.html"
    success_url = reverse_lazy("productos:lista")
    permission_required = "productos.change_producto"

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente.")
        return super().form_valid(form)


class ProductoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Producto
    template_name = "productos/confirmar_borrado.html"
    success_url = reverse_lazy("productos:lista")
    permission_required = "productos.delete_producto"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Producto eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


class ProductoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Producto
    template_name = "productos/detalle.html"
    context_object_name = "producto"
    permission_required = "productos.view_producto"


