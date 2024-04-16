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
from assignment2_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'page2/?$', views.page2, name='page2'),
    re_path(r'about/?$', views.about, name='about'),
    path('page3/<int:thesisid>/', views.show_thesis_topic),
    re_path(r'/?$', views.home, name = 'homepage'), ## made for the homepage appearing in the localhost:8000 - VG
]

urlpatterns += staticfiles_urlpatterns()