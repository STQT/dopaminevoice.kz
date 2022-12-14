from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("manga/", TemplateView.as_view(template_name="pages/manga.html"), name="manga"),
    path("news/", include("news.urls", namespace="news"), name="news"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin_async_upload/', include('admin_async_upload.urls')),
    path("", include("movies.urls", namespace="movies")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
