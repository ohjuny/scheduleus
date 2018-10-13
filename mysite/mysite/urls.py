"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

# import views from apps
from home import views as home_views
from accounts import views as accounts_views
from events import views as events_views

urlpatterns = [
    # Django admin
    url(r'^admin/', admin.site.urls),

    # Home app
    url(r'^$', home_views.home, name="home"),

    # Accounts app
    url(r'^signup/$', accounts_views.signup, name="signup"),

    # Events app
    url(r'^create/$', events_views.create, name="create"),
]
