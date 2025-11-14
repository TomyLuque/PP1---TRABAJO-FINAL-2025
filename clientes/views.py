from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Cliente
from .forms import ClienteForm


class ClienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Cliente
    template_name = "clientes/lista.html"
    context_object_name = "clientes"
    paginate_by = 10
    permission_required = "clientes.view_cliente"

    def get_queryset(self):
        queryset = Cliente.objects.all().order_by("apellido")

        nombre = self.request.GET.get("nombre", "")
        documento = self.request.GET.get("documento", "")

        if nombre:
            from django.db.models import Q
            queryset = queryset.filter(
                Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre)
            )

        if documento:
            queryset = queryset.filter(documento__icontains=documento)

        return queryset


class ClienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("clientes:lista")
    permission_required = "clientes.add_cliente"

    def form_valid(self, form):
        messages.success(self.request, "Cliente creado correctamente.")
        return super().form_valid(form)


class ClienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("clientes:lista")
    permission_required = "clientes.change_cliente"

    def form_valid(self, form):
        messages.success(self.request, "Cliente actualizado correctamente.")
        return super().form_valid(form)


class ClienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Cliente
    template_name = "clientes/confirmar_borrado.html"
    success_url = reverse_lazy("clientes:lista")
    permission_required = "clientes.delete_cliente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado correctamente.")
        return super().delete(request, *args, **kwargs)


class ClienteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Cliente
    template_name = "clientes/detalle.html"
    context_object_name = "cliente"
    permission_required = "clientes.view_cliente"
