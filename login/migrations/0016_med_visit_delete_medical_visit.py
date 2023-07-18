# Generated by Django 4.2.1 on 2023-06-07 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_medical_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='med_visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('diagnosis', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='login.medical_condition')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.medical')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.inmate')),
            ],
        ),
        migrations.DeleteModel(
            name='Medical_visit',
        ),
    ]
