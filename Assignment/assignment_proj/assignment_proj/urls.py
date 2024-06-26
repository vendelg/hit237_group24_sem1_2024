"""
URL configuration for assignment_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from assignment2_app import views  # Correct import statement
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from assignment2_app.views import ChangePasswordView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^page2/?$', views.page2, name='page2'),
    re_path(r'^about/?$', views.about, name='about'),
    path('page3/<tid>/', views.show_thesis_topic, name='details'),
    path('modify/thesis/<tid>/', views.modify_thesis, name='modify_thesis'),
    re_path(r'^$', views.home, name='homepage'),
    path('add/thesis/', views.add_thesis, name='add_thesis'),
    path('add/thesis/request/', views.add_thesis_request),
    re_path(r'^edit/thesis/(?P<key>\d+)?/?$', views.edit_thesis),
    # re_path(r'^delete/thesis/(?P<key>\d+)?/?$', views.delete_publisher),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('apply/thesis/<tid>/', views.thesis_application, name='application_form'),
    path('apply/notice/', views.application_submit, name='applicationnotice'),
    path('register/student/', views.student_registration, name='registerform'),
    path('register/student/done/', views.registration_submit, name='registrationdone'),
    path('dashboard/<user_id>/', views.dashboard, name='dashboard'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'), 
    path('notification/<int:user_id>/', views.notification, name='notification'),
     path('request/<tid>', views.Requests, name='Requests'),

]

urlpatterns += staticfiles_urlpatterns()
