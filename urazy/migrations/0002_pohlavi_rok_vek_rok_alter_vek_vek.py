# Generated by Django 5.1.3 on 2024-11-26 20:10


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urazy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pohlavi',
            name='rok',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='vek',
            name='rok',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vek',
            name='vek',
            field=models.CharField(max_length=10),
        ),
    ]
