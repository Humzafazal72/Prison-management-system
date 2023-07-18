# Generated by Django 4.2.1 on 2023-06-02 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_shift_remove_admin_gender_remove_inmate_gender_co'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_conditions',
            fields=[
                ('Condition_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('CO_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('dob', models.DateField()),
                ('title', models.CharField(max_length=32)),
                ('contact_number', models.CharField(max_length=11)),
                ('salary', models.BigIntegerField()),
                ('password', models.CharField(max_length=8)),
                ('patients', models.ManyToManyField(blank=True, related_name='doctor', to='login.inmate')),
                ('shift', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='login.shift')),
            ],
        ),
        migrations.AddField(
            model_name='inmate',
            name='medical_cond',
            field=models.ManyToManyField(blank=True, related_name='patient', to='login.medical_conditions'),
        ),
    ]
