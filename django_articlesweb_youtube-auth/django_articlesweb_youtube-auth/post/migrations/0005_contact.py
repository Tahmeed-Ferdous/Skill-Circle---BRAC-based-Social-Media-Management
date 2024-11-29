# Generated by Django 3.0.4 on 2020-03-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('message_date', models.DateField()),
                ('message', models.TextField(max_length=3000)),
            ],
        ),
    ]