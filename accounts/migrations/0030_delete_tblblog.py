# Generated by Django 5.1.2 on 2025-02-06 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_rename_blogdate_tblblog_blogurl_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TblBlog',
        ),
    ]
