# Generated by Django 2.1.3 on 2018-11-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeda_app', '0009_auto_20181126_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]