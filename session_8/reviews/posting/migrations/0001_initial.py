# Generated by Django 3.0.6 on 2020-05-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
