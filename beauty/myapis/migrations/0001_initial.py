# Generated by Django 4.0.5 on 2022-06-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('alias', models.CharField(max_length=100)),
                ('super_power', models.CharField(choices=[('FLY', 'FLY'), ('RUN FAST', 'RUN FAST'), ('SHOOTING WEB', 'SHOOTING WEB'), ('STRONG', 'STRONG')], max_length=50)),
            ],
        ),
    ]