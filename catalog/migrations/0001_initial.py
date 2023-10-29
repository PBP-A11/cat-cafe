# Generated by Django 4.2.6 on 2023-10-29 15:40


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='N/A', max_length=255)),
                ('author', models.CharField(default='N/A', max_length=255)),
                ('preview_link', models.URLField(default='N/A')),
                ('description', models.TextField(default='N/A')),
                ('category', models.CharField(default='N/A', max_length=10)),
                ('rating', models.CharField(default='N/A', max_length=10)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('date_published', models.CharField(max_length=20)),
                ('image_link', models.URLField(default='N/A')),
            ],
        ),
    ]
