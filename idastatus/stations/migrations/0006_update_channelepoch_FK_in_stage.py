# Generated by Django 2.2.13 on 2020-09-02 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_fix_names_from_datascope_to_obspy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='channel_epoch',
            field=models.ForeignKey(help_text='Channel Epoch FK', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stage_list', to='stations.ChannelEpoch'),
        ),
    ]
