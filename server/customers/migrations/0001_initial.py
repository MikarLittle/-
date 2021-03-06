# Generated by Django 2.1 on 2018-08-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=20)),
                ('parent_name', models.CharField(blank=True, max_length=20, null=True)),
                ('classin_id', models.CharField(blank=True, max_length=20, null=True)),
                ('classin_name', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('audition_count', models.IntegerField(default=0)),
                ('is_signedup', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('date_cc', models.DateField(blank=True, null=True)),
                ('demand', models.TextField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=6, null=True)),
            ],
        ),
    ]
