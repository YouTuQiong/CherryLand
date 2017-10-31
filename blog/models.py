from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils.html import format_html
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# 标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Month(models.Field):
    description = "A hand of cards (bridge style)"

    def __init__(self, *args, **kwargs):
        self.editable = False
        super(Month, self).__init__(*args, **kwargs)


class Article(models.Model):
    # 文章头照片
    head_Img = FilerImageField(null=True, blank=True,
                           related_name="head_Article")
    # 文章所需要的图片
    disclaimer = FilerFileField(null=True, blank=True,
                                related_name="disclaimer_Article")
    # 文章标题
    title = models.CharField(max_length=70, verbose_name='标题')
    # 文章正文，
    body = models.TextField(verbose_name='正文')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    # 创建时间自动写
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='最后修改时间')

    # 文章摘要
    excerpt = models.TextField(verbose_name='摘要')

    # 这是分类与标签
    # 我们规定一篇文章一个分类，一个分类多篇文章，即一对多的关联关系。
    # 篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 一对多关系，和 Category 类似。
    author = models.ForeignKey(User, verbose_name='作者')
    # 阅读量
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def retrunHTMLForBody(self):
        return format_html(self.body)  # 使用html转义而不是在模板中使用safe，防止xss攻击

    def retrunHTMLForE(self):
        return format_html(self.excerpt)  # 使用html转义而不是在模板中使用safe，防止xss攻击

# 注册用户，这里我们使用了Consumer因为User Django已经有了。为了不冲突
class  Consumer(models.Model):
    # id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=64,verbose_name="用户名")
    Email = models.EmailField(max_length=64,verbose_name="邮箱")
    Password  =models.CharField(max_length=64,verbose_name="密码")
    #IsAvailable = models.BooleanField(default=True)
    #AddTime = models.DateTimeField(auto_now_add=True,verbose_name="注册时间")
    #HeadURL
class Login(models.Model):
    UserId = models.BigIntegerField(verbose_name="用户ID")
    Sessionid = models.CharField(max_length=32,verbose_name="session")#有可能没有
    Csrftoken = models.CharField(max_length=64, verbose_name="Csrftoken")
    COMPUTERNAME = models.CharField(max_length=128,verbose_name="计算机域")
    USERNAME = models.CharField(max_length=128,verbose_name="设备名")
    IpAddress = models.GenericIPAddressField(verbose_name="ip地址")
    HTTP_USER_AGENT = models.CharField(max_length=128,verbose_name="登陆头")
    HTTP_REFERER  = models.CharField(max_length=128,verbose_name="登录页面")
    LoginTime = models.DateTimeField(verbose_name="登录时间")
class Discuss(models.Model):
    Article = models.BigIntegerField(max_length=10,verbose_name="文章ID")
    IsShow = models.BooleanField(default=True,verbose_name="是否显示")
    AddTime = models.DateTimeField(auto_now_add=True)
    UserID = models.BigIntegerField(verbose_name="用户ID")

# 喜欢的句子
class LikePhrase(models.Model):
    phrase = models.TextField()

    def __str__(self):
        return self.phrase

    # def retrunHTML(self):
    #     return format_html(self.phrase)  # 使用html转义而不是在模板中使用safe，防止xss攻击
    #



#分页
class JuncheePaginator(Paginator):
    def __init__(self, object_list, per_page, range_num=5, orphans=0, allow_empty_first_page=True):
        Paginator.__init__(self, object_list, per_page, orphans, allow_empty_first_page)
        self.range_num = range_num

    def page(self, number):
        self.page_num = number
        return super(JuncheePaginator, self).page(number)

    def _page_range_ext(self):
        num_count = 2 * self.range_num + 1
        if self.num_pages <= num_count:
            return range(1, self.num_pages + 1)
        num_list = []
        num_list.append(self.page_num)
        for i in range(1, self.range_num + 1):
            if self.page_num - i <= 0:
                num_list.append(num_count + self.page_num - i)
            else:
                num_list.append(self.page_num - i)

            if self.page_num + i <= self.num_pages:
                num_list.append(self.page_num + i)
            else:
                num_list.append(self.page_num + i - num_count)
        num_list.sort()
        return num_list

    page_range_ext = property(_page_range_ext)
