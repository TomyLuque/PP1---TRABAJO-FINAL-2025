from django.db import migrations

def create_default_groups(apps, schema_editor):
    from django.contrib.auth.models import Group
    for name in ['administradores', 'stock', 'ventas']:
        Group.objects.get_or_create(name=name)

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]
    operations = [
        migrations.RunPython(create_default_groups),
    ]
