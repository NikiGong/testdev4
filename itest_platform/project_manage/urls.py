from django.urls import path
from project_manage.views import manage_views

urlpatterns = [
    path('', manage_views.manage),  # 二级路径为空的话，直接返回manage
    path('add/', manage_views.project_add),
    # path('/edit/', manage_views.edit),
    # path('/delete/', manage_views.delete),
]
