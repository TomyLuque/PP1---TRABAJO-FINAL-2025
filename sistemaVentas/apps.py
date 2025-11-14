from django.apps import AppConfig

class SistemaVentasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sistemaVentas" 

    def ready(self):
        import sistemaVentas.signals
