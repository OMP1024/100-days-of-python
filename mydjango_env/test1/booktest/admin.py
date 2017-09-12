from django.contrib import admin

# Register your models here.

from django.contrib import admin
from booktest.models import BookInfo
admin.site.register(BookInfo)

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]

admin.site.register(BookInfo,BookInfoAdmin)
