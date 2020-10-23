from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import BabyTrack, Baby
from .forms import EntryForm

def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "Saved!!")
            return redirect('index')
            
        
        messages.warning(request, "Not Saved!!")
        
    form = EntryForm()
    return render(request, 'index.html', {'form':form})

def entries(request):
    entries = BabyTrack.objects.order_by('-date')
    context = {
        'entries':entries
    }
    return render(request, 'entries.html', context)

def babies(request):
    babies = Baby.objects.all()
    context = {
        'babies':babies
    }
    return render(request, 'babies.html', context)