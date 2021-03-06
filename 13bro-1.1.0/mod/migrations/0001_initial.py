# Generated by Django 2.0.7 on 2018-07-18 07:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='正文')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '发表')], default='p', max_length=1, verbose_name='状态')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('pub_time', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('picture', models.ImageField(default='image/ad.jpg', upload_to='static', verbose_name='图片')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章列表',
                'db_table': 'article',
                'ordering': ['-pub_time'],
                'get_latest_by': 'created_time',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='分类名')),
            ],
            options={
                'verbose_name': '分类名',
                'verbose_name_plural': '分类列表',
                'db_table': 'category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ChiCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='子类名')),
                ('first_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.Category', verbose_name='子类名')),
            ],
            options={
                'verbose_name': '子类名',
                'verbose_name_plural': '子类名',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('pwd', models.CharField(max_length=255, verbose_name='用户密码')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='chicategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod.ChiCategory', verbose_name='分类'),
        ),
    ]
