# Generated by Django 4.1.3 on 2022-12-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0007_alter_message_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
