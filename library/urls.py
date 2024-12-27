from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from ckeditor_uploader import views as ckeditor_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('category/<int:category_id>/', views.document_list, name='document_by_category'),
    path('<int:pk>/', views.document_detail, name='document_detail'),    
    path('upload/', views.upload_document, name='upload_document'),
    path('<int:pk>/edit/', views.edit_document, name='edit_document'),
    path('<int:pk>/delete/', views.delete_document, name='delete_document'),
    path('document/<int:pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    # CKEditor 관련 URL
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', csrf_exempt(ckeditor_views.upload), name='ckeditor_upload'),
]

# 정적 파일 및 미디어 파일 제공
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)