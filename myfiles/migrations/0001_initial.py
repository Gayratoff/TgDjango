# Generated by Django 4.1.3 on 2022-12-22 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('money', models.IntegerField()),
                ('chegirma_money', models.IntegerField(blank=True, null=True)),
                ('rasm_link', models.CharField(max_length=100)),
                ('malumot', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.menu')),
            ],
        ),
    ]
