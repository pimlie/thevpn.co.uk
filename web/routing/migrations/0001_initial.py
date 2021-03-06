# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 11:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_ca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.IntegerField()),
                ('shortname', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dns', models.CharField(default='no.hostname.provided', max_length=255)),
                ('description', models.TextField()),
                ('endpointkey', models.CharField(max_length=256)),
                ('radiuskey', models.CharField(max_length=64)),
                ('auto_connect', models.BooleanField(default=True)),
                ('ASN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routing.AS')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ca.Certificate')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routing.Country')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RouterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VPNProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('shortname', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VPNServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField()),
                ('protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routing.VPNProtocol')),
            ],
        ),
        migrations.AddField(
            model_name='router',
            name='routertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routing.RouterType'),
        ),
        migrations.AddField(
            model_name='router',
            name='supported_client_vpn_protocols',
            field=models.ManyToManyField(blank=True, to='routing.VPNProtocol'),
        ),
        migrations.AddField(
            model_name='router',
            name='supported_server_vpn_protocols',
            field=models.ManyToManyField(blank=True, to='routing.VPNServer'),
        ),
    ]
