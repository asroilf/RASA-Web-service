# Generated by Django 5.0.6 on 2024-06-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1024)),
                ('response', models.CharField(default='HI', max_length=2000)),
            ],
        ),
    ]