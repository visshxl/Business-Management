# Generated by Django 5.1.1 on 2024-11-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_data',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]
