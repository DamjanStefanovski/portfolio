# Generated by Django 2.0.2 on 2018-05-21 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20180518_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]