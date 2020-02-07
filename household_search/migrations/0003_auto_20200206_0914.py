# Generated by Django 3.0.3 on 2020-02-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household_search', '0002_auto_20200206_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='housing_type',
            field=models.IntegerField(choices=[(1, 'HDB'), (2, 'Landed'), (3, 'Condominium')]),
        ),
    ]