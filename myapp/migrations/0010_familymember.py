# Generated by Django 3.2.20 on 2024-04-16 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='familymember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=25)),
                ('adhar', models.CharField(max_length=25)),
                ('relation', models.CharField(max_length=25)),
                ('CARDHOLDER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cardholder')),
            ],
        ),
    ]