from django.contrib import admin
from .models import Category, Document, File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')  # 목록에서 순서 확인
    list_editable = ('order',)  # 목록에서 순서 편집 가능

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'document')
    search_fields = ('file',)
