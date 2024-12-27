from django.shortcuts import render
from .views_CpaBongHistory import *

# Create your views here.

def about_cpabong(request):

    context = {
        '선민위원경력사항' : 선민위원경력사항,
        '선민Work경력사항' : 선민Work경력사항,
        '정윤위원경력사항' : 정윤위원경력사항,
        '정윤Work경력사항' : 정윤Work경력사항,
        '로이드세부경력' : 로이드세부경력,
        '한영재무자문' : 한영재무자문,
        '한영감사본부' : 한영감사본부,
    }

    print(context)
    return render(request, 'aboutbong/aboutBong.html', context)