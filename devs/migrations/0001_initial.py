# Generated by Django 5.1.3 on 2024-11-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotodev', models.ImageField(blank=True, null=True, upload_to='devs/')),
                ('nombredev', models.TextField()),
                ('apellidodev', models.TextField()),
                ('numerodev', models.TextField()),
                ('nocontroldev', models.TextField()),
                ('correoddev', models.TextField()),
            ],
        ),
    ]
