# Generated by Django 3.1.6 on 2021-02-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientInfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
