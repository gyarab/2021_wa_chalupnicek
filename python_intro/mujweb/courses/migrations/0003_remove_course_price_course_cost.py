# Generated by Django 4.0.1 on 2022-02-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.AddField(
            model_name='course',
            name='cost',
            field=models.CharField(default='10 EUR', max_length=255),
            preserve_default=False,
        ),
    ]
