from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choices
    extra = 1

class QuestionAdmin(ModelAdmin):
    inlines = [ChoiceInline]
class ChoiceAdmin(ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin),
admin.site.register(Choices, ChoiceAdmin)
admin.site.register(User)