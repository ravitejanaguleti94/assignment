# Generated by Django 4.1.5 on 2023-01-25 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departments',
            options={'verbose_name_plural': 'Departments'},
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.departments')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]
