from layver_project import settings

__author__ = 'la0rg'

from django.conf.urls import patterns, url
from layver import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.main_page, name="main_page"),
    url(r'^newpage/$', views.screens_view, name="new_page"),
    url(r'^result/(?P<pk>\d+)/$', views.ResultView.as_view(), name="results"),
    url(r'^makescreenshots/(?P<id>\d+)/$', views.make_screenshots, name="make_screenshots"),

    url(r'^start_layers$', views.layer_page, name="layer_page"),
    url(r'^layers_view/$', views.layer_view, name="layers_view"),
    url(r'^layers/(?P<pk>\d+)/$', views.ErrorsView.as_view(), name="errors"),
    url(r'^tagerrors/(?P<id>\d+)/$', views.tag_errors, name="tag_errors"),

    url(r'^page_list/$', views.PageListView.as_view(), name="page_list_view"),
)