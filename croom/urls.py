"""croom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from chat import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   url(r'^admin/', admin.site.urls),
    url(r'^$', views.server_list, name='server_list'),
    url(r'^log/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'server_list.html'}, name='logout'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^register/$', views.signup, name='signup'),
    url(r'^functions/$', views.Function, name='Function'),
	url(r'^Ateacher1/$', views.Ateacher12, name='Ateacher12'),
	url(r'^Ateacher/$', views.Ateacher1, name='Ateacher1'),
	#url(r'^class/$', views.class1, name='class1'),
	url(r'^Ainvites/$', views.SubscriptionView, name='SubscriptionView'),
	url(r'^create/$', views.server_create, name='server_create'),
	url(r'^edit/(?P<pk>\d+)$', views.server_update, name='user_edit'),
	#url(r'^Ainvites/$', views.class1, name='class1'),
	url('^api/v1/', include('social_django.urls', namespace='social')),
	#url(r'^chat/$', views.Home, name='home'),
	url(r'^chat1/$', views.Messages, name='home'),
    url(r'^', include('chat.urls')),
	url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
	url(r'^class/(?P<pk>\d+)$', views.Home, name='home'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

