# Generated by Django 3.2.7 on 2021-09-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=150)),
                ('gender', models.CharField(choices=[('', 'Not specified'), ('female', 'Female'), ('male', 'Male')], max_length=50)),
                ('company', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
            ],
            options={
                'verbose_name_plural': 'customers',
            },
        ),
    ]
