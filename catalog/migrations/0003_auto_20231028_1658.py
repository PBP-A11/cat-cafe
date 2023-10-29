from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command('loaddata', 'booksfinal.json')

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
