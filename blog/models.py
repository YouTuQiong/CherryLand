from django.db import models
from django.contrib.auth.models import User
from django.db.models import Field
from django.urls import reverse
from django.core.paginator import Paginator
from django.utils.html import format_html
from filer.fields.image import FilerImageField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class f(models.Model):
    logo = FilerImageField(null=True, blank=True,
                           related_name="logo_company")


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
    # 文章标题
    title = models.CharField(max_length=70, verbose_name='标题')
    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(verbose_name='正文')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='最后修改时间')
    # Month.get_lookup(created_time.date().month + created_time.date().day)
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.TextField(verbose_name='摘要')

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 官方文档：https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User, verbose_name='作者')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def retrunHTMLForBody(self):
        return format_html(self.body)  # 使用html转义而不是在模板中使用safe，防止xss攻击

    def retrunHTMLForE(self):
        return format_html(self.excerpt)  # 使用html转义而不是在模板中使用safe，防止xss攻击


# 喜欢的橘子
class LikePhrase(models.Model):
    phrase = models.TextField()

    def __str__(self):
        return self.phrase

    # def retrunHTML(self):
    #     return format_html(self.phrase)  # 使用html转义而不是在模板中使用safe，防止xss攻击
    #

from django.db import models


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
