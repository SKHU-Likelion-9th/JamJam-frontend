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
    path('signup', jamjamapp.views.signup, name='signup'),
    path('findpw', jamjamapp.views.findpw, name='findpw'),
    path('main/', jamjamapp.views.main, name='main'),
    path('community/', jamjamapp.views.community, name='community'),
    path('commu_write/', jamjamapp.views.commu_write, name='commu_write'),
    path('commu_edit/', jamjamapp.views.commu_edit, name='commu_edit'),
    path('commu_detail/', jamjamapp.views.commu_detail, name='commu_detail'),
    path('mypage/', jamjamapp.views.mypage, name='mypage'),
    path('profile/', jamjamapp.views.profile, name='profile'),
    path('connection', jamjamapp.views.connection, name='connection'),
    path('purchaselist', jamjamapp.views.purchaselist, name='purchaselist'),
    path('profile_edit/', jamjamapp.views.profile_edit, name='profile_edit'),
    path('day_detail/', jamjamapp.views.day_detail, name='day_detail'),
    path('theme/', jamjamapp.views.theme, name='theme'),
    path('course/', jamjamapp.views.course, name='course'),
    path('course_detail/', jamjamapp.views.course_detail, name='course_detail'),
    path('course_write/', jamjamapp.views.course_write, name='course_write'),
    path('course_edit/', jamjamapp.views.course_edit, name='course_edit'),
    path('purchase_example/', jamjamapp.views.purchase_example, name='purchase_example'),
    path('diary/', jamjamapp.views.diary, name='diary'),
    path('option/', jamjamapp.views.option, name='option'),
    path('shop/', jamjamapp.views.shop, name='shop'),
    path('diary_edit/', jamjamapp.views.diary_edit, name='diary_edit'),
    path('jampay/', jamjamapp.views.jampay, name='jampay'),
    path('scrap/', jamjamapp.views.scrap, name='scrap'),
    path('pay/', jamjamapp.views.pay, name='pay'),
    path('completepay/',jamjamapp.views.completepay, name='completepay'),
    path('bookmark_category/', jamjamapp.views.bookmark_category, name='bookmark_category'),
    path('bookmark_create/', jamjamapp.views.bookmark_create, name='bookmark_create'),
    path('bookmark_delete/', jamjamapp.views.bookmark_delete, name='bookmark_delete'),
    path('bookmark_detail/', jamjamapp.views.bookmark_detail, name='bookmark_detail'),
    path('bookmark_list/', jamjamapp.views.bookmark_list, name='bookmark_list'),
    path('bookmark_update/', jamjamapp.views.bookmark_update, name='bookmark_update'),
]