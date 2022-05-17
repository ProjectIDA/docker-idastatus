# Generated by Django 2.2.18 on 2022-04-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0018_increase_leading_factor_again'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='gnom',
            field=models.DecimalField(blank=True, decimal_places=8, help_text='Nominal sensitivity', max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='stage',
            name='leading_factor',
            field=models.DecimalField(blank=True, decimal_places=9, default=None, help_text='Leading Factor', max_digits=25, null=True),
        ),
    ]