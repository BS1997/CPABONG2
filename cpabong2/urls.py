from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from ckeditor_uploader import views as ckeditor_views
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path("kmobsk/", admin.site.urls),
    path('members/', include('members.urls')),
    path('', include('main.urls')),
    path('about/', include('aboutbong.urls')),
    path('apps/', include('Apps.urls')),
    path('library/', include('library.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', csrf_exempt(ckeditor_views.upload), name='ckeditor_upload'),
    # 미디어 파일 서빙을 위한 URL 패턴 추가
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)