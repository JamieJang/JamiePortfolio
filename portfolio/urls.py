from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('resume.urls',namespace="resume")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
