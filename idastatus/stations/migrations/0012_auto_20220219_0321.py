# Generated by Django 2.2.18 on 2022-02-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0011_stage_leading_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='leading_factor',
            field=models.FloatField(blank=True, default=None, help_text='Leading Factor', null=True),
        ),
    ]
