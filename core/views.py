from django.shortcuts import render

def api_root(request):
    return render(request, 'api_root.html')