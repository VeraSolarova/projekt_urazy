# Generated by Django 5.1.3 on 2024-11-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]


    operations = [
        migrations.CreateModel(
            name='Pohlavi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pohlavi', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Vek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vek', models.CharField(max_length=5)),
            ],
        ),
    ]
