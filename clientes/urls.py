from django.urls import path
from .views import (
    ClienteListView, ClienteCreateView, ClienteUpdateView,
    ClienteDeleteView, ClienteDetailView
)

app_name = "clientes"

urlpatterns = [
    path("", ClienteListView.as_view(), name="lista"),
    path("nuevo/", ClienteCreateView.as_view(), name="crear"),
    path("<int:pk>/editar/", ClienteUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", ClienteDeleteView.as_view(), name="eliminar"),
    path("<int:pk>/", ClienteDetailView.as_view(), name="detalle"),
]
