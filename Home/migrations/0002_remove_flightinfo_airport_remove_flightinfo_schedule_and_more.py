# Generated by Django 4.1.3 on 2022-12-28 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightinfo',
            name='airport',
        ),
        migrations.RemoveField(
            model_name='flightinfo',
            name='schedule',
        ),
        migrations.AddField(
            model_name='flightinfo',
            name='fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Home.schedule'),
            preserve_default=False,
        ),
    ]