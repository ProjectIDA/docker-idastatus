# Generated by Django 2.2.2 on 2020-05-12 02:24

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
                ('altcode', models.CharField(blank=True, max_length=4, null=True)),
                ('code', models.CharField(blank=True, help_text='Network code', max_length=4, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, help_text='Network description', max_length=100, null=True)),
                ('histcode', models.CharField(blank=True, max_length=50, null=True)),
                ('begt', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('endt', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr1', models.CharField(blank=True, default=None, help_text='Address field 1', max_length=50, null=True)),
                ('addr2', models.CharField(blank=True, default=None, help_text='Address field 2', max_length=50, null=True)),
                ('altcode', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('city', models.CharField(blank=True, default=None, help_text='City', max_length=50, null=True)),
                ('code', models.CharField(help_text='Station code', max_length=6)),
                ('country', models.CharField(blank=True, default=None, help_text='Country', max_length=50, null=True)),
                ('country_code', models.CharField(default=None, help_text="Station's country code", max_length=2, null=True)),
                ('description', models.CharField(blank=True, default=None, help_text='Station description', max_length=100, null=True)),
                ('elev', models.FloatField(default=None, help_text='Elevation', null=True)),
                ('begt', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('endt', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('geo_datum', models.CharField(blank=True, choices=[('ONE', 'First One'), ('TWO', 'Second One'), ('THREE', 'Third One')], help_text='Geodetic Positioning System', max_length=50, null=True)),
                ('geology_descr', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('histcode', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('lat', models.FloatField(default=None, help_text='Latitude', null=True)),
                ('lddate', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('loc_descr', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('lon', models.FloatField(default=None, help_text='Longitude', null=True)),
                ('staname', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('postal_code', models.CharField(blank=True, default=None, help_text='Postal Code', max_length=15, null=True)),
                ('province', models.CharField(blank=True, default=None, help_text='Province', max_length=50, null=True)),
                ('status_code', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('status_descr', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('status_updated', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('vault_descr', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('network_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stations.Network')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decifac', models.BigIntegerField()),
                ('dfile', models.CharField(blank=True, max_length=64, null=True)),
                ('dir', models.CharField(blank=True, max_length=128, null=True)),
                ('gcalib', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('gnom', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('iunits', models.CharField(blank=True, max_length=200, null=True)),
                ('ounits', models.CharField(blank=True, max_length=200, null=True)),
                ('srate', models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True)),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
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
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
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
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelEpoch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altcode', models.CharField(blank=True, max_length=4, null=True)),
                ('chan', models.CharField(blank=True, max_length=8, null=True)),
                ('code', models.CharField(blank=True, help_text='ChannelEpoch code', max_length=4, null=True)),
                ('edepth', models.FloatField(null=True)),
                ('begt', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('endt', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=17, null=True)),
                ('flag', models.CharField(blank=True, max_length=10, null=True)),
                ('hang', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, help_text='Epoch description', max_length=100, null=True)),
                ('histcode', models.CharField(blank=True, max_length=50, null=True)),
                ('instype', models.CharField(blank=True, max_length=12, null=True)),
                ('storage_format', models.CharField(blank=True, choices=[('ONE', 'First One'), ('TWO', 'Second One'), ('THREE', 'Third One')], help_text='Storage Format', max_length=50, null=True)),
                ('string', models.CharField(blank=True, max_length=200, null=True)),
                ('vang', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('loc', models.CharField(blank=True, max_length=2, null=True)),
                ('nomfreq', models.FloatField(default=None, help_text='Longitude', null=True)),
                ('station_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stations.Station')),
            ],
        ),
    ]
