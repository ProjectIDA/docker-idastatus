# Generated by Django 2.2.2 on 2019-08-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_auto_20190722_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelEpoch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altcode', models.CharField(blank=True, max_length=4, null=True)),
                ('chn', models.CharField(blank=True, max_length=4, null=True)),
                ('edepth', models.FloatField(blank=True, null=True)),
                ('end_t', models.DateTimeField(blank=True, null=True)),
                ('flags', models.CharField(blank=True, max_length=200, null=True)),
                ('hang', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, help_text='Network description', max_length=200, null=True)),
                ('end_date', models.DateField(blank=True, help_text='Last valid time for data', null=True)),
                ('histcode', models.CharField(blank=True, max_length=50, null=True)),
                ('start_t', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altcode', models.CharField(blank=True, max_length=4, null=True)),
                ('code', models.CharField(blank=True, help_text='Station code', max_length=4, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, help_text='Network description', max_length=200, null=True)),
                ('end_date', models.DateField(blank=True, help_text='Last valid time for data', null=True)),
                ('histcode', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='addr1',
            field=models.CharField(blank=True, help_text='Address field 1', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='addr2',
            field=models.CharField(blank=True, help_text='Address field 2', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='altcode',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='city',
            field=models.CharField(blank=True, help_text='City', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='country',
            field=models.CharField(blank=True, help_text='Country', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='elev',
            field=models.FloatField(blank=True, help_text='Elevation', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='end_t',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='geology_descr',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='histcode',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='lat',
            field=models.FloatField(blank=True, help_text='Latitude', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='loc_descr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='lon',
            field=models.FloatField(blank=True, help_text='Longitude', null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='network_id',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='postal_code',
            field=models.CharField(blank=True, help_text='Postal Code', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='province',
            field=models.CharField(blank=True, help_text='Province', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='start_t',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=17, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='status_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='status_descr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='status_updated',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='vault_descr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='code',
            field=models.CharField(blank=True, help_text='Station code', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='country_code',
            field=models.CharField(blank=True, help_text="Station's country code", max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.CharField(blank=True, help_text='Station description', max_length=200, null=True),
        ),
    ]
