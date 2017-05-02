from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.chatter_list_view, name='list'),
    #url(r'^1/$', views.chatter_detail_view, name='detail'),
    url(r'^$', views.ChatterListView.as_view(), name='list'),
    url(r'^create/$', views.ChatterCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ChatterDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ChatterUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ChatterDeleteView.as_view(), name='delete'),
]
