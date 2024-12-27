from django.shortcuts import render
from .calc import *
# Create your views here.

def AppStockValuation(request):
    send_vars = {}
    if request.method == 'GET':        
        send_vars['msg'] = 'sj_light input'
        
        send_vars['submitted'] = False
    
    if request.method == 'POST':
        send_vars['msg'] = 'sj_light output'
        send_vars['submitted'] = True
        for key, value in calculate_simple(request).items():
            send_vars[key] = value
        
        for key, value in send_vars.items():
            print(key, value)
            
    
    return render(request, 'Apps/AppStockValuation.html', {'vars':send_vars})