# Generated by Django 2.1 on 2018-11-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0005_auto_20181120_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompareSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('java', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
