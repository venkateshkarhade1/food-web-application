# Generated by Django 4.0.1 on 2022-03-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='descr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dec', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
                ('pname', models.TextField()),
            ],
        ),
    ]
