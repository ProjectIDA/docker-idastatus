# Generated by Django 2.2.18 on 2022-04-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0019_increase_gnom_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='leading_factor',
            field=models.DecimalField(blank=True, decimal_places=9, default=None, help_text='Leading Factor', max_digits=30, null=True),
        ),
    ]