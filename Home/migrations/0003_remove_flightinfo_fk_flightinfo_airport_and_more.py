# Generated by Django 4.1.3 on 2022-12-28 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_flightinfo_airport_remove_flightinfo_schedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightinfo',
            name='fk',
        ),
        migrations.AddField(
            model_name='flightinfo',
            name='airport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.airport'),
        ),
        migrations.AddField(
            model_name='flightinfo',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.schedule'),
        ),
    ]