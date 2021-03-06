from django.db import models
from django.utils.timezone import now


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名', unique=True)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    pwd = models.CharField(max_length=255, verbose_name='用户密码')


# class Tag(models.Model):
#     name = models.CharField(max_length=64, verbose_name='标签名')
#     create_time = models.DateTimeField(verbose_name='创建时间', default=now)
#     last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)
#
#     # 使对象在后台显示更友好
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = '标签名称'  # 指定后台显示模型名称
#         verbose_name_plural = '标签列表'  # 指定后台显示模型负数名称
#         db_table = 'tag'  # 数据库表名


class Category(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='分类名')

    class Meta:
        ordering = ['name']
        verbose_name = '分类名'  # 指定后台显示模型名称
        verbose_name_plural = '分类列表'  # 指定后台显示模型复数名称
        # 数据库表名
        db_table = 'category'

    # 使对象在后台显示更友好
    def __str__(self):
        return self.name


# class ChiCategory(models.Model):
#     # id = models.AutoField(primary_key=True)
#     first_type = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='所属分类')
#     # 级联删除, 如果父表中的记录被删除，则子表中对应的记录自动被删除
#     name = models.CharField(verbose_name='子类名', max_length=64)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = '子类名'
#         verbose_name_plural = '子类列表'
#         db_table = 'chicategory'


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    # id = models.AutoField(primary_key=True) 不设定主键则自动生成
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='正文', blank=True, null=True)
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    views = models.PositiveIntegerField(verbose_name='浏览量', default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    pub_time = models.DateTimeField(verbose_name='发布时间', blank=True, null=True)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)
    picture = models.ImageField(verbose_name='图片', upload_to='images/artpic', blank=True)
    category = models.ForeignKey(Category, verbose_name='所属分类', on_delete=models.CASCADE,
                                 default=None, blank=False, null=False)
    # 设定一个点赞的字段，限定显示数量等
    good_count = models.IntegerField(default=0, db_column='tgcount', verbose_name='点赞数')

    def __str__(self):
        return self.title

    # 限定点赞最大数量
    @property
    def gcount(self):
        return f'{self.good_count}' \
            if self.good_count <= 999999 else '999999+'

    # 刷新浏览量
    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def next_article(self):  # id比当前id大，状态为已发布，发布时间不为空
        return Article.objects.filter(id__gt=self.id, status='p', pub_time__isnull=False).first()

    def prev_article(self):  # id比当前id小，状态为已发布，发布时间不为空
        return Article.objects.filter(id__lt=self.id, status='p', pub_time__isnull=False).first()

    class Meta:
        ordering = ['create_time']  # 按发布时间降序
        verbose_name = '文章'  # 指定后台显示的模型名称
        verbose_name_plural = '文章列表'  # 指定后台显示模型负数名称
        db_table = 'article'  # 数据库表名
        get_latest_by = 'created_time'


# 点赞函数建模，包含IP地址、关联文章、点击时间
class Poll(models.Model):
    ip = models.CharField(max_length=100, null=True, blank=True)
    art = models.ForeignKey(Article, on_delete=models.CASCADE)
    click_time = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.art)


# 评论函数建模，包含ip、昵称、内容、创建时间、关联文章外键、自己关联自己外键（可在评论上回复）
class Comments(models.Model):
    ip = models.CharField(max_length=100, null=True, blank=True)
    nickname = models.CharField(max_length=40, verbose_name='昵称')
    content = models.TextField(max_length=400, verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Article, related_name='b', on_delete=models.CASCADE)
    reply = models.ForeignKey('Comments', related_name='r', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
