# Generated by Django 4.2.7 on 2023-12-19 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_profil_manzil_profil_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='rasm',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
