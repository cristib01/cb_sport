# Generated by Django 5.0.1 on 2024-01-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('abonare', 'Abonare'), ('accesoriu', 'Accesoriu')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]