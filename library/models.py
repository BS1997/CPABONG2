from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User  # 사용자 모델 import

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 카테고리 이름
    description = models.TextField(blank=True, null=True)  # 카테고리 설명
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일시
    order = models.PositiveIntegerField(default=0)  # 순서 필드 추가

    class Meta:
        ordering = ['order']  # 기본 정렬 기준 설정
        
    def __str__(self):
        return self.name

class Document(models.Model):
    id = models.AutoField(primary_key=True)  # 명시적으로 pk 필드 추가
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents'
    )  # 카테고리 추가
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class File(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file.name

class Comment(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='document_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # 최신 댓글이 먼저 보이도록

    def __str__(self):
        return f'Comment by {self.author} on {self.document}'