# Generated by Django 4.2.1 on 2023-06-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_education_inmate_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmate',
            name='completed_courses',
            field=models.ManyToManyField(blank=True, related_name='completed', to='login.education'),
        ),
    ]
