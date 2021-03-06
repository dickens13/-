# Generated by Django 2.0.7 on 2018-07-18 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod', '0004_auto_20180718_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='chicategory',
            name='first_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.Category', verbose_name='所属分类'),
        ),
    ]
