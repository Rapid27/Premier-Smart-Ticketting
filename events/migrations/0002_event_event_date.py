# Generated by Django 4.1.2 on 2022-11-21 12:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="Event_Date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Event Date"
            ),
            preserve_default=False,
        ),
    ]
