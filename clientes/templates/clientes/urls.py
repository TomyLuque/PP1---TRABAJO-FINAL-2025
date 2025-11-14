from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='clientes_lista'),
    path('nuevo/', views.ClienteCreateView.as_view(), name='clientes_nuevo'),
    path('editar/<int:pk>/', views.ClienteUpdateView.as_view(), name='clientes_editar'),
    path('borrar/<int:pk>/', views.ClienteDeleteView.as_view(), name='clientes_borrar'),
]
