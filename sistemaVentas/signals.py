# sistemaVentas/signals.py
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

@receiver(post_migrate)
def crear_grupos(sender, **kwargs):
    if sender.name == "auth":  # se ejecuta después de migrar el módulo de auth
        grupos = {
            "administradores": {
                "permisos": Permission.objects.all()
            },
            "stock": {
                "permisos": Permission.objects.filter(content_type__app_label__in=["productos"])
            },
            "ventas": {
                "permisos": Permission.objects.filter(content_type__app_label__in=["clientes", "ventas"])
            },
        }

        for nombre, config in grupos.items():
            grupo, creado = Group.objects.get_or_create(name=nombre)
            grupo.permissions.set(config["permisos"])
            grupo.save()
            print(f"✅ Grupo '{nombre}' creado o actualizado")
