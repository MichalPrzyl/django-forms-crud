"""formsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from first_app.views import list_people, add_new_person_template, add_new_person, delete_person, edit_person, edit_person_template
urlpatterns = [
    path('admin/', admin.site.urls),
    path("list", list_people),
    path("add_new_person_template", add_new_person_template),
    path("add_new_person", add_new_person),
    path("delete_person/<int:pk>", delete_person),
    path("edit_person_template/<int:pk>", edit_person_template),
    path("edit_person/<int:pk>", edit_person),
    
]
