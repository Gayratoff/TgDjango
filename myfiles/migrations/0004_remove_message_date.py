# Generated by Django 4.1.3 on 2022-12-22 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_alter_maxsulot_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
    ]