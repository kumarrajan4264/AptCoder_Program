"""AptCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage2/', views.homepage2, name='homepage2'),
    path('aboutPage/', views.aboutpage, name='aboutpage'),
    path('coursesPage/', views.coursespage, name='coursespage'),
    path('kiddoPage/', views.kiddopage, name='kiddopage'),
    path('buddyPage/', views.buddypage, name='buddypage'),
    path('proPage/', views.propage, name='propage'),
    path('trialPage/', views.trialpage, name='trialpage'),
    path('blogPage/', views.blogpage, name='blogpage'),
    path('contactPage/', views.contactpage, name='contactpage'),
    path('singleBlogPage/', views.singleblogpage, name='singleblogpage'),
    path('elementsPage/', views.elementspage, name='elementspage'),
    path('courseDetailsPage/', views.coursedetailspage, name='coursedetailspage'),
    path('chartPage/', views.chartpage, name='chartpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('buddy2/', views.buddy2, name='buddy2'),
]
