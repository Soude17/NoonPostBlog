# Generated by Django 5.1.3 on 2025-03-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال'),
        ),
    ]
