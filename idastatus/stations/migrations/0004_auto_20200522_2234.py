# Generated by Django 2.2.11 on 2020-05-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_auto_20200522_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stage',
            old_name='dir',
            new_name='sp_dir',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='dfile',
            new_name='sp_filename',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='stage_gain',
        ),
        migrations.AddField(
            model_name='stage',
            name='gcalib',
            field=models.DecimalField(blank=True, decimal_places=5, help_text='Calibration sensitivity factor', max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='gnom',
            field=models.DecimalField(blank=True, decimal_places=5, help_text='Nominal sensitivity', max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='ssident',
            field=models.CharField(blank=True, help_text='Serial Number (or other identifier)', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='izero',
            field=models.IntegerField(blank=True, help_text='index of FIR coeff. for 0th sample', null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='stageid',
            field=models.IntegerField(blank=True, help_text='Stage index for parent ChannelEpoch (cascade)', null=True),
        ),
    ]
