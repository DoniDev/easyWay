# Generated by Django 3.0.8 on 2020-07-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200719_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test_field',
            field=models.TextField(blank=True, default=''),
        ),
    ]
