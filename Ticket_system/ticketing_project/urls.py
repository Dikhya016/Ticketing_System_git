"""
URL configuration for ticketing_project project.

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
from django.urls import path
from tickets import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
#from .import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/',views.LoginPage, name='login'),
    #path('index/', views.open_index, name='open_index'),
    path('logout/',views.LogoutPage, name='logout'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('list/', views.list_tickets, name='list_tickets'),
    path('<int:ticket_id>/', views.view_edit_ticket, name='view_edit_ticket'),
    path('search/', views.search_ticket, name='search_ticket'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
