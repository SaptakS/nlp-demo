# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	(r'^nlp/', include('myproject.myapp.urls')),
	(r'^$', RedirectView.as_view(url='/nlp/home/')), # Just for ease of use.
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
