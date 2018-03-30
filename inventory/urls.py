from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetail.as_view(), name='specific-tag'),
    url(r'^items/(?P<pk>[0-9]+)$', views.ItemDetail.as_view(), name='specific-item'),
    url(r'^items/$', views.ItemList.as_view(), name='list-item'),
    url(r'^loans/$', views.LoanList.as_view(), name='list-loan'),
    url(r'^tags/$', views.TagList.as_view(), name='list-tag'),
]
