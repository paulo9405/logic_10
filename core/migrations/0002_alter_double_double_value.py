# Generated by Django 4.0.6 on 2022-07-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='double',
            name='double_value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]