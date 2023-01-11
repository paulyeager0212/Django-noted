from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.i18n import JavaScriptCatalog
from django.urls import path, include

from content.sitemaps import NoteSitemap, SourceSitemap


sitemaps = {
    "notes": NoteSitemap,
    "sources": SourceSitemap,
}


urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("users/", include(("users.urls", "users"), namespace="users")),
    path("tags/", include(("tags.urls", "tags"), namespace="tags")),
    path("jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("", include(("content.urls", "content"), namespace="content")),
)

urlpatterns += [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    # TODO: test https://adamj.eu/tech/2020/02/10/robots-txt/
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain"
        ),
    ),
]


handler400 = "core.views.handler400"
handler403 = "core.views.handler403"
handler404 = "core.views.handler404"
handler500 = "core.views.handler500"

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns.insert(1, path("rosetta/", include("rosetta.urls")))

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
