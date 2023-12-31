# Generated by Django 4.2.4 on 2023-08-24 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('joined_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('worked_on', models.TextField()),
                ('screenshot', models.ImageField(upload_to='screenshots/')),
                ('intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.intern')),
            ],
        ),
    ]
