# Generated by Django 3.1.4 on 2020-12-15 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_board_main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='email',
        ),
    ]
