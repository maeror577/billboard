# Generated by Django 3.2.3 on 2021-05-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]