# Generated by Django 4.2.1 on 2023-06-08 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0017_remove_inmate_medical_cond_alter_med_visit_diagnosis_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='co',
            name='title',
        ),
    ]
