from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag,LikePhrase
from django_summernote.admin import SummernoteModelAdmin
# admin.site.register(Article)

from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'modified_time')
    list_display_links = ('id', 'title')
    list_select_related = ('author', 'category')
    search_fields = ('title', 'body')
class PageModelAdmin(SummernoteModelAdmin):
    pass
class Article_and_PageModelAdmin(ArticleAdmin,PageModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(LikePhrase,PageModelAdmin)
admin.site.register(Article,Article_and_PageModelAdmin)

