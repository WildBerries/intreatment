from django.conf.urls import url

from . import views as appoint


urlpatterns = [url(r'^$', appoint.setAppointment, name='appointment')
    ]
