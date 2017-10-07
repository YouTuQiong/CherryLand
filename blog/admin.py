from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag,LikePhrase
from django_summernote.admin import SummernoteModelAdmin
# admin.site.register(Article)

from django_summernote.admin import SummernoteModelAdmin
class PageModelAdmin(SummernoteModelAdmin):
    pass
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(LikePhrase,PageModelAdmin)
admin.site.register(Article,PageModelAdmin)
