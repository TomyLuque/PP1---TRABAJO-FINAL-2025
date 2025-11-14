from django.urls import path
from . import views

urlpatterns = [
    path('', views.VentaListView.as_view(), name='ventas_lista'),
    path('nuevo/', views.nueva_venta, name='ventas_nueva'),
    path('borrar/<int:pk>/', views.VentaDeleteView.as_view(), name='ventas_borrar'),
    path('<int:pk>/', views.VentaDetalleView.as_view(), name='ventas_detalle'),
]

