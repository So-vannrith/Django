# Generated by Django 5.1.2 on 2025-02-06 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_tblblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblblog',
            name='BlogDescription',
        ),
    ]
