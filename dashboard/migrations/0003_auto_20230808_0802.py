# Generated by Django 3.2.16 on 2023-08-08 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chalantable',
            name='amount',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chalantable',
            name='qty',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chalantable',
            name='rate',
            field=models.TextField(blank=True, null=True),
        ),
    ]
