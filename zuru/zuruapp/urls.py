from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url('^event/(\d+)', views.events, name='events'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)