# Generated by Django 2.2.18 on 2022-02-19 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0010_auto_20220208_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='leading_factor',
            field=models.DecimalField(blank=True, decimal_places=5, help_text='Leading Factor', max_digits=17, null=True),
        ),
    ]
