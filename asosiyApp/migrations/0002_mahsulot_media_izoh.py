# Generated by Django 4.2.7 on 2023-11-28 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('brend', models.CharField(max_length=255)),
                ('narx', models.PositiveIntegerField()),
                ('chegirma', models.PositiveIntegerField(default=0)),
                ('batafsil', models.TextField()),
                ('kafolat', models.CharField(max_length=255)),
                ('yetkazish', models.CharField(max_length=255)),
                ('mavjud', models.BooleanField(default=True)),
                ('davlat', models.CharField(max_length=255)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyApp.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyApp.mahsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
                ('baho', models.PositiveIntegerField(default=5)),
                ('sana', models.DateField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyApp.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]