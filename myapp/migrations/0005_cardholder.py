# Generated by Django 3.2.20 on 2024-03-25 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_suplyco'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=100)),
                ('hname', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=100)),
                ('adhar', models.CharField(max_length=100)),
                ('AREA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.area')),
                ('CARDTYPE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.rationcardtype')),
            ],
        ),
    ]
