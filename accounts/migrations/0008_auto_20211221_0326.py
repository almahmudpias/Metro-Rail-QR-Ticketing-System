# Generated by Django 3.2.10 on 2021-12-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211221_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='booking_id',
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
