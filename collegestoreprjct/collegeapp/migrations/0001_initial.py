# Generated by Django 4.2.4 on 2023-11-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('age', models.TextField()),
                ('dob', models.CharField(max_length=250)),
                ('gender', models.TextField()),
                ('phone', models.TextField()),
                ('mailid', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('dept', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('puropose', models.TextField()),
                ('mat_provd', models.TextField()),
            ],
        ),
    ]
