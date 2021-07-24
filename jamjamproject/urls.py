"""jamjamproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import jamjamapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jamjamapp.views.layout1, name='layout1'),
    path('layout2/', jamjamapp.views.layout2, name='layout2'),
    path('login', jamjamapp.views.login, name='login'),
    path('main/', jamjamapp.views.main, name='main'),
    path('community/', jamjamapp.views.community, name='community'),
    path('commu_write/', jamjamapp.views.commu_write, name='commu_write'),
    path('commu_edit/', jamjamapp.views.commu_edit, name='commu_edit'),
    path('detail/', jamjamapp.views.detail, name='detail'),
]
