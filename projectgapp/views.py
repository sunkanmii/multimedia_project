from django.shortcuts import render
from .models import MediaFiles
# Create your views here.
def HomeView(req):
    data = MediaFiles.objects.all()
    return render(req, 'index.html', {'data': data})