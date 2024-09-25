# Generated by Django 5.1.1 on 2024-09-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epsignalapp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_type', models.CharField(choices=[('technique', 'Problème Technique'), ('physique', 'Problème Physique')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('incident_date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Probleme',
        ),
    ]
