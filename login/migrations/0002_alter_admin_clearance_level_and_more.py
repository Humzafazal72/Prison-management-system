# Generated by Django 4.2.1 on 2023-06-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='clearance_level',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='admin',
            name='contact_number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='inmate',
            name='Risk_level',
            field=models.SmallIntegerField(),
        ),
    ]
