from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
#django自带的后台管理操作需要在此实现
#注册自己需要管理的模型，book，hero
from .models import Book, Hero


class HeroInline(admin.StackedInline):
    '''
    定义关联类
    '''
    model = Hero
    extra = 5


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')


admin.site.register(Hero, HeroAdmin)

class BookAdmin(ModelAdmin):

    list_display = ('title', 'price', 'pub_date')
    list_per_page = 2
    search_fields = ('title', 'price', 'pub_date')
    list_filter = ('title', 'price')

    inlines = [HeroInline]


admin.site.register(Book,BookAdmin)

