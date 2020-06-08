from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'auth/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'auth/logout.html'),name='logout'),
    re_path(r'^project/(\d+)',views.project,name ='project'),
    re_path(r'^new_projects$', views.new_projects, name='new_projects'),
    re_path(r'^profile/(\d+)', views.profile, name='profile'),
    re_path(r'^edit_profile/$',views.edit_profile,name = 'newedit_profile'),
    re_path(r'^myprojects/$',views.myprojects,name = 'myprojects'),
    re_path(r'^search/', views.search, name='search'),
    re_path(r'^new/rating/(\d+)',views.newrating, name='newrating'),
    re_path(r'^api/profile/$', views.ProfileList.as_view()),
    re_path(r'^api/project/$', views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)