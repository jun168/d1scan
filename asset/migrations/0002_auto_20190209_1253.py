# Generated by Django 2.1.5 on 2019-02-09 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DnsList',
            new_name='DomainList',
        ),
        migrations.AlterModelOptions(
            name='domainlist',
            options={},
        ),
    ]