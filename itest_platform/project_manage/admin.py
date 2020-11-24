from django.contrib import admin
from project_manage.models import Project,Module

# Register your models here.
# 把models创建的表快速映射到admin后台

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time', 'update_time']   # 把表的哪个字段映射到admin后台


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'describe', 'create_time', 'update_time']


admin.site.register(Project, ProjectAdmin)  # 注册到admin后台
admin.site.register(Module, ModuleAdmin)