# Generated by Django 3.1.4 on 2021-07-17 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='aksh1/'),
            preserve_default=False,
        ),
    ]
