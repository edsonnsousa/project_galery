# Generated by Django 3.2.7 on 2021-09-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_image_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tipo',
            field=models.IntegerField(blank=True, default=2),
        ),
    ]
