# Generated by Django 4.2.3 on 2023-10-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='Unique_no',
            new_name='unique_no',
        ),
        migrations.RemoveField(
            model_name='students',
            name='Sr_No',
        ),
        migrations.AddField(
            model_name='students',
            name='unique_no',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='unique_no'),
            preserve_default=False,
        ),
    ]
