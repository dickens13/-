# Generated by Django 2.0.7 on 2018-08-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0016_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='ip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
