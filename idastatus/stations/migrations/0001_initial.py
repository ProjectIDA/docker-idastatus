# Generated by Django 2.2.2 on 2020-05-14 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, help_text='Network code', max_length=4, null=True)),
                ('description', models.CharField(blank=True, help_text='Network description', max_length=100, null=True)),
                ('end_date', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('start_date', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Station code', max_length=6)),
                ('elevation', models.FloatField(default=None, help_text='Station Elevation', null=True)),
                ('start_date', models.DecimalField(blank=True, decimal_places=5, default=None, help_text='Station Start Date', max_digits=17, null=True)),
                ('end_date', models.DecimalField(blank=True, decimal_places=5, default=None, help_text='Station End Date', max_digits=17, null=True)),
                ('latitude', models.FloatField(default=None, help_text='Station Latitude', null=True)),
                ('longitude', models.FloatField(default=None, help_text='Station Longitude', null=True)),
                ('site', models.CharField(blank=True, default=None, help_text='Station Site Information', max_length=200, null=True)),
                ('network', models.ForeignKey(help_text='Station Network ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='stations.Network')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decimation_factor', models.BigIntegerField()),
                ('data_file_name', models.CharField(blank=True, max_length=64, null=True)),
                ('data_dir', models.CharField(blank=True, max_length=128, null=True)),
                ('stage_gain', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('input_units', models.CharField(blank=True, max_length=200, null=True)),
                ('output_units', models.CharField(blank=True, max_length=200, null=True)),
                ('decimation_input_sample_rate', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('station', models.ForeignKey(help_text='Station ID', on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
            ],
        ),
        migrations.CreateModel(
            name='IrisWithdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chan', models.CharField(blank=True, max_length=4, null=True)),
                ('endt', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('loc', models.CharField(blank=True, max_length=2, null=True)),
                ('sta', models.CharField(blank=True, max_length=4, null=True)),
                ('begt', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
            ],
        ),
        migrations.CreateModel(
            name='IrisEpoch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chan', models.CharField(blank=True, max_length=4, null=True)),
                ('decimal', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('endt', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('loc', models.CharField(blank=True, max_length=2, null=True)),
                ('sta', models.CharField(blank=True, max_length=4, null=True)),
                ('begt', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelEpoch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, help_text='ChannelEpoch code', max_length=4, null=True)),
                ('depth', models.FloatField(null=True)),
                ('start_date', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('end_date', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('types', models.CharField(blank=True, max_length=10, null=True)),
                ('azimuth', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('sensor', models.CharField(blank=True, max_length=12, null=True)),
                ('dip', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('location_code', models.CharField(blank=True, max_length=2, null=True)),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
            ],
        ),
    ]
