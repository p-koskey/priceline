# Generated by Django 3.1.3 on 2020-11-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carhire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('Petrol', 'P'), ('Diesel', 'D')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Manual', 'M'), ('Auto', 'A')], max_length=300, null=True),
        ),
    ]