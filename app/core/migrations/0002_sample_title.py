# Generated by Django 3.2.18 on 2023-04-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]