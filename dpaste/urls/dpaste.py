from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static
#from django.contrib.staticfiles import views as static_views

from .. import views
from .. import contribute

L = getattr(settings, 'DPASTE_SLUG_LENGTH', 4)

urlpatterns = [
    url(r'^$', views.SnippetView.as_view(), name='snippet_new'),
    #url(
    #    r'^static/(?P<path>.*)$',
    #    static_views.serve,
    #),
    url(
        r'^about/$',
        TemplateView.as_view(template_name='dpaste/about.html'),
        name='dpaste_about',
    ),
    url(r'^history/$', views.SnippetHistory.as_view(), name='snippet_history'),
    url(
        r'^(?P<snippet_id>[a-zA-Z0-9]{%d,})/?$' % L,
        views.SnippetDetailView.as_view(),
        name='snippet_details',
    ),
    url(
        r'^(?P<snippet_id>[a-zA-Z0-9]{%d,})/raw/?$' % L,
        views.SnippetRawView.as_view(),
        name='snippet_details_raw',
    ),
    url(
        r'^contribute.json$',
        contribute.contrib_file,
        name='contrib_file',
    ),
]
