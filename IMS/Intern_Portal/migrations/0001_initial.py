# Generated by Django 4.2.2 on 2023-08-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('department', models.CharField(default='Student', max_length=100)),
            ],
            options={
                'db_table': 'Student_Profile',
            },
        ),
    ]