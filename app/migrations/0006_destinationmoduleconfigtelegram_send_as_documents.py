# Generated by Django 3.0.2 on 2020-01-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200119_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationmoduleconfigtelegram',
            name='send_as_documents',
            field=models.BooleanField(default=False),
        ),
    ]
