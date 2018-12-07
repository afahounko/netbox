# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 16:35
from django.db import migrations
import utilities.fields


COLOR_CONVERSION = {
    'teal': '009688',
    'green': '4caf50',
    'blue': '2196f3',
    'purple': '9c27b0',
    'yellow': 'ffeb3b',
    'orange': 'ff9800',
    'red': 'f44336',
    'light_gray': 'c0c0c0',
    'medium_gray': '9e9e9e',
    'dark_gray': '607d8b',
}


def color_names_to_rgb(apps, schema_editor):
    RackRole = apps.get_model('dcim', 'RackRole')
    DeviceRole = apps.get_model('dcim', 'DeviceRole')
    for color_name, color_rgb in COLOR_CONVERSION.items():
        RackRole.objects.filter(color=color_name).update(color=color_rgb)
        DeviceRole.objects.filter(color=color_name).update(color=color_rgb)


def color_rgb_to_name(apps, schema_editor):
    RackRole = apps.get_model('dcim', 'RackRole')
    DeviceRole = apps.get_model('dcim', 'DeviceRole')
    for color_name, color_rgb in COLOR_CONVERSION.items():
        RackRole.objects.filter(color=color_rgb).update(color=color_name)
        DeviceRole.objects.filter(color=color_rgb).update(color=color_name)


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0021_add_ff_flexstack'),
    ]

    operations = [
        migrations.RunPython(color_names_to_rgb, color_rgb_to_name),
        migrations.AlterField(
            model_name='devicerole',
            name='color',
            field=utilities.fields.ColorField(max_length=6),
        ),
        migrations.AlterField(
            model_name='rackrole',
            name='color',
            field=utilities.fields.ColorField(max_length=6),
        ),
    ]
