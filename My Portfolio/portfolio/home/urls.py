from django.contrib import admin
from django.urls import path, include
from home import views


# django Admin header customization.

admin.site.site_header = "Developer Rushi"
admin.site.site_title = "Welcome to Rushi's Dashboard"
admin.site.index_title = "Welcome to the Portal"
 


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
]
