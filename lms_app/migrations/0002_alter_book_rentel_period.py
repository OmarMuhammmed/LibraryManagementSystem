# Generated by Django 5.0.2 on 2024-04-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rentel_period',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
