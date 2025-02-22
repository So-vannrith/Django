# Generated by Django 5.1.2 on 2025-01-30 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_tblfooter_footername'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerName', models.CharField(max_length=200, null=True)),
                ('img1', models.ImageField(upload_to='logoImg')),
                ('img2', models.ImageField(upload_to='logoImg')),
                ('img3', models.ImageField(upload_to='logoImg')),
                ('img4', models.ImageField(upload_to='logoImg')),
                ('text1', models.CharField(max_length=200, null=True)),
                ('text2', models.CharField(max_length=200, null=True)),
                ('span1', models.CharField(max_length=200, null=True)),
                ('span2', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
