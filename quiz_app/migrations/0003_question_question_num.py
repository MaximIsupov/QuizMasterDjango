# Generated by Django 3.2.9 on 2022-01-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_auto_20220104_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_num',
            field=models.IntegerField(default=0),
        ),
    ]
