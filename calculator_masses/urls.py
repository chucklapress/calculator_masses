"""calculator_masses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout


from calcapp.views import home_view, app_view, user_create_view, profile_view






urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, name='index_view'),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^user_create/$', user_create_view, name='user_create_view'),
    url(r'^home/$', home_view, name='home_view'),
    url(r'^app/$', app_view, name='app_view'),
    url(r'^accounts/profile/$',profile_view, name="profile_view")




]
