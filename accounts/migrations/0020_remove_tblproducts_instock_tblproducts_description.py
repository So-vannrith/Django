# Generated by Django 5.1.2 on 2025-01-26 14:31

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_tblblogtype_tblblog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblproducts',
            name='instock',
        ),
        migrations.AddField(
            model_name='tblproducts',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
