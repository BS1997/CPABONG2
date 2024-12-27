from django import forms
from .models import Comment
from .models import Document, File
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # 올바른 위젯 임포트

class DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())  # CKEditorUploadingWidget 사용

    class Meta:
        model = Document
        fields = ['title', 'description', 'category']  # category 필드 추가

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }