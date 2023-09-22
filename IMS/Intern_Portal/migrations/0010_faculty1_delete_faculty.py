# Generated by Django 4.2.2 on 2023-08-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0009_alter_faculty_date_of_joining'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('faculty_name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField()),
                ('qualification', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('upload', models.FileField(blank=True, null=True, upload_to='faculty_excel/')),
            ],
            options={
                'db_table': 'Faculty',
            },
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
    ]