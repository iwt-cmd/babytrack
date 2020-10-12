from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import BabyTrack, Baby
from .forms import PostForm

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('entries')
    else:
        form = PostForm()
    return render(request, 'index.html', {'form':form})

def entries(request):
    entries = BabyTrack.objects.order_by('-date')
    context = {
        'entries':entries
    }
    return render(request, 'entries.html', context)