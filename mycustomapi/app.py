from django.conf.urls import url
from oscarapi.app import RESTApiApplication

from . import views

class MyRESTApiApplication(RESTApiApplication):

   def get_urls(self):
    urls = [
        url(r'^users/$', views.UserList.as_view(), name='user-list'),
        url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),        
    ]

    return urls + super(MyRESTApiApplication, self).get_urls()

application = MyRESTApiApplication()
