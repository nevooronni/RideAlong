from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^accounts',include('registration.backends.simple.urls')),
    url(r'^new/driver',views.register_driver,name = 'register_driver'),
    url(r'^login/driver',views.login_driver,name = 'login_driver'),
    url(r'^driver/(\d+)',views.driver,name = 'driver'),
    url(r'^page',views.page,name = 'page'),
    url(r'^new/rider',views.register_rider,name = 'register_rider'),
    url(r'^login/rider',views.login_rider,name = "login_rider"),
    url(r'^rider/(\d+)',views.rider,name = 'rider'),
    url(r'^edit/driver/profile(\d+)',views.edit_driver_profile,name="edit_driver_profile")
]

if settings.DEBUG == True:
	urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)