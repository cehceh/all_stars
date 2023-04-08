from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home_page(request):
    data = {}
    data['error'] = ''
    data['msg'] = ''
    # data['type'] = 'error'
    if request.accepts('text/plain') and request.method == 'POST':
        data['error'] = 'Unforunatly I have to learn selenium, But It is not available now' 
        data['msg'] = 'But I am good in Ajax, Jquery, Javascript, Postgresql and Django'
        # data['type'] = 'error'
        return JsonResponse(data)


    return render(request, 'home/home.html', {})

