from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Document, File, Category, Comment
from .forms import DocumentForm, FileForm, CommentForm  
from django.forms import modelformset_factory
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def document_list(request, category_id=None):
    categories = Category.objects.annotate(document_count=Count('documents')).order_by('order')  # 문서 개수 추가
    print(categories)
    if category_id:
        # 선택한 카테고리에 해당하는 문서만 필터링
        documents = Document.objects.filter(category_id=category_id).order_by('-uploaded_at')
        selected_category = get_object_or_404(Category, id=category_id)  # 선택된 카테고리
    else:
        # 모든 문서 표시
        documents = Document.objects.all().order_by('-uploaded_at')
        selected_category = None

    total_document_count = Document.objects.count()  # 전체 문서 개수 계산

    return render(request, 'library/document_list.html', {
        'documents': documents,
        'categories': categories,
        'selected_category': selected_category,
        'total_document_count': total_document_count,  # 전체 문서 개수 전달
    })


def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    comments = document.comments.all()  # 해당 문서의 모든 댓글
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.document = document
            comment.author = request.user
            comment.save()
            return redirect('document_detail', pk=pk)
    else:
        form = CommentForm()
        
    return render(request, 'library/document_detail.html', {
        'document': document,
        'comments': comments,
        'form': form,
    })

@login_required
def delete_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
    return redirect('document_detail', pk=pk)


def upload_document(request):
    if request.user.username != 'qhdtn6412':
        return redirect('document_list')  # 다른 페이지로 리디렉션

    FileFormSet = modelformset_factory(File, form=FileForm, extra=3)  # 최대 3개의 파일 추가
    if request.method == 'POST':
        document_form = DocumentForm(request.POST)
        file_formset = FileFormSet(request.POST, request.FILES, queryset=File.objects.none())
        if document_form.is_valid() and file_formset.is_valid():
            document = document_form.save()
            for form in file_formset:
                if form.cleaned_data.get('file'):
                    file = form.save(commit=False)
                    file.document = document
                    file.save()
            return redirect('document_list')
    else:
        document_form = DocumentForm()
        file_formset = FileFormSet(queryset=File.objects.none())
    return render(request, 'library/upload_document.html', {
        'document_form': document_form,
        'file_formset': file_formset
    })

def edit_document(request, pk):
    if request.user.username != 'qhdtn6412':
        return redirect('document_list')  # 다른 페이지로 리디렉션

    document = get_object_or_404(Document, pk=pk)
    FileFormSet = modelformset_factory(File, form=FileForm, extra=0)
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, instance=document)
        file_formset = FileFormSet(request.POST, request.FILES, queryset=document.files.all())
        if document_form.is_valid() and file_formset.is_valid():
            document = document_form.save()
            for form in file_formset:
                if form.cleaned_data.get('file'):
                    file = form.save(commit=False)
                    file.document = document
                    file.save()
            return redirect('document_detail', pk=document.pk)
    else:
        document_form = DocumentForm(instance=document)
        file_formset = FileFormSet(queryset=document.files.all())
    return render(request, 'library/edit_document.html', {
        'document_form': document_form,
        'file_formset': file_formset,
        'document': document,  # 템플릿에 전달
    })

def delete_document(request, pk):
    if request.user.username != 'qhdtn6412':
        return redirect('document_list')  # 다른 페이지로 리디렉션

    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'library/delete_document.html', {'document': document})