# Generated by Django 4.2.6 on 2023-10-29 15:40

from django.db import migrations
from django.core.management import call_command
from django.contrib.auth.hashers import make_password
import json
import os


def load_my_initial_data(apps, schema_editor):
    script_dir = os.path.dirname(os.path.realpath(__file__))

    relative_path = os.path.join('..', 'fixtures', 'initial_admin.json')
    absolute_path = os.path.join(script_dir, relative_path)

    with open(absolute_path, 'r') as file:
        data = json.load(file)
        
    data[0]['fields']['password'] = make_password('pbp12345')

    with open(absolute_path, 'w') as file:
        json.dump(data, file, indent=2) 

    call_command("loaddata", "initial_admin.json")

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
