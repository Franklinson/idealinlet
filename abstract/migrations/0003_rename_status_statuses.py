# Generated by Django 4.2.10 on 2024-02-21 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0002_rename_abstract_form_abstract_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status',
            new_name='Statuses',
        ),
    ]
