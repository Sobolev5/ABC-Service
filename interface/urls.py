import debug_toolbar
import settings
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.conf.urls.static import static
from api.handlers import api_handlers
from api_drf.urls import router as drf_router
from api_drf import views_without_router as drf_views_without_router 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("i18n/", include("django.conf.urls.i18n"))
]

# pet
urlpatterns += [
    path(r"api/", api_handlers.urls),
    path(r"education/", include("education.urls", namespace="education")),
]

# drf
urlpatterns += [
    path("api-drf/", include(drf_router.urls)),
    path("api-drf-as-cbv/topic/", drf_views_without_router.TopicList.as_view()),
    path("api-drf-as-cbv/topic/<int:pk>/", drf_views_without_router.TopicDetail.as_view()),    
]

urlpatterns += [
    re_path(r"", include("main.urls", namespace="main")),
    re_path(r"chat/", include("chat.urls", namespace="chat")),
    re_path(r"^profile/", include("user_profile.urls", namespace="user_profile")),
]

# format_suffix_patterns(urlpatterns) https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/format-suffixes ??????

handler404 = "main.views.handler404"
handler500 = "main.views.handler500"


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
