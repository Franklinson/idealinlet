# Generated by Django 4.2.10 on 2024-02-26 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0019_abstract_editors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstract',
            name='editors',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]