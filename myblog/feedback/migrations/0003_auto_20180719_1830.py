# Generated by Django 2.0.6 on 2018-07-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feed_back',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='text',
            name='mob_no',
            field=models.CharField(max_length=10),
        ),
    ]