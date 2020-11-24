"""itest_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from project_manage.views import login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', login_views.hello),
    path('', login_views.index), # 不输入详细路径时，直接去到index页面
    path('index/', login_views.index),
    # path('login/', views.login)
    # path('manage/', views.manage),
    # path('/manage/add', views.manage),
    # path('/manage/edit', views.manage),
    # path('/manage/delete', views.manage),
    path('manage/', include('project_manage.urls')),  # 如果匹配到manage路径，直接project_manage.urls找路径

    # path('/logout/', login_views.logout),
]
