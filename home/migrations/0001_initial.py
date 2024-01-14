# Generated by Django 5.0.1 on 2024-01-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
                ('DetectionType', models.CharField(max_length=100)),
                ('User', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Severity', models.CharField(max_length=50)),
                ('ProcessName', models.CharField(max_length=200)),
                ('Path', models.CharField(max_length=500)),
                ('DetectionOrigin', models.CharField(max_length=100)),
                ('Message', models.TextField()),
                ('AlertTime', models.DateTimeField()),
            ],
        ),
    ]
