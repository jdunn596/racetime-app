# Generated by Django 3.0.2 on 2020-05-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0030_auto_20200509_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='detailed_timer',
            field=models.BooleanField(default=True, help_text='Show tenths of a second on the race timer. You can also click on the race timer to switch between detailed and simple mode.'),
        ),
    ]