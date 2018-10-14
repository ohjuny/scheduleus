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
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.conf.urls.static import static

# import views from apps
from home import views as home_views
from accounts import views as accounts_views
from events import views as events_views
from sms import views as sms_views

urlpatterns = [
    # Django admin
    url(r'^admin/', admin.site.urls),

    # Home app
    url(r'^$', home_views.home, name="home"),

    # Accounts app
    url(r'^signup/$', accounts_views.signup, name="signup"),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Events app
    url(r'^create/$', events_views.create, name="create"),
    url(r'^events/$', events_views.events, name="events"),
    url(r'^event/(?P<eventID>.+)/$', events_views.event, name="event"),

    url(r'^ajax/search_users/$', events_views.search_users, name='search_users'),

    # SMS app
    url(r'^sms/$', csrf_exempt(sms_views.sms), name="sms"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
