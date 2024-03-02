# Generated by Django 4.2.10 on 2024-02-26 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('abstract', '0018_alter_abstract_abstract_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='assigned_abstracts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='presentation_preference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='abstract.presentation_type'),
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
