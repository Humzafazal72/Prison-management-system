# Generated by Django 4.2.1 on 2023-06-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_alter_visitor_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmate',
            name='charges',
            field=models.ManyToManyField(blank=True, related_name='criminal', to='login.charge'),
        ),
    ]
