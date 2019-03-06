from django.contrib import admin
from . import models
# Register your models here.

# @admin.register(models.Users)
class UserAdmin(admin.ModelAdmin):
    # # 指定展示列表
    list_display = ['name','age']
    # # # 过滤器
    # list_filter = ['age']
    # # # 指定分页
    # list_per_page =3
    # # # 指定修改属性
    # fields = ['age']
    # # 选中前面的选框，可以做一些动作
    # actions_on_bottom = True
    # actions_on_top = False
    # # 通过姓名或年龄查找
    # search_fields = ['name','age']
    # # 设置可以点击进入编辑界面，默认是第一选项
    # list_display_links = ['name','age']
    # # ordering设置默认排序字段，负号表示降序排列
    # ordering = ('-age','-name')
    # 默认设置可编辑字段，这个与list_display_links相冲突
    list_editable = ['age']
# 使文章的题目和内容显示
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content']

admin.site.register(models.Users,UserAdmin)
admin.site.register(models.Article,ArticleAdmin)



