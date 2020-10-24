from django.shortcuts import render
from .models import Baby

def babies(request):
    
    babies = Baby.objects.all()
    context = {
        'babies':babies
    }
    
    return render(request, 'babies.html', context)