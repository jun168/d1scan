# Generated by Django 2.1.5 on 2019-02-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20190209_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainlist',
            name='domain',
            field=models.CharField(max_length=50, unique=True, verbose_name='域名'),
        ),
    ]