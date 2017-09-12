from django.contrib import admin
from .models import Question,Choice

# 关联对象，以栈的形式展示
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     # 后台管理界面中默认显示三个 Choice
#     extra = 3

# 关联对象，以表格的形式展示
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 自定义管理界面的外观和功能
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']

    # fieldsets = [(None,{'fields': ['question_text']}),
    #              ('Date Infomation',{'fields':['pub_date']}

    # fieldsets = [(None,{'fields':['question_text']}),
    #              ('发布日期',{'fields':['pub_date'],'classes':['collapse']}),]

    list_display = ('question_text','pub_date','was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']

    # Question 关联上 Choice
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Question,QuestionAdmin)
