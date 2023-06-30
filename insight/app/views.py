from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

# Create your views here.


def home(request):
    articles = Articles.objects.all()
    context = {'articles': articles}
    return render(request, 'app/home.html', context)


def addarticle(request):
    form = ArticlesForm()
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'app/addarticle.html', context)


def updatearticle(request, pk):
    article = Articles.objects.get(id=pk)
    form = ArticlesForm(instance=article)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            print('invalid')
    context = {'form': form}
    return render(request, 'app/addarticle.html', context)


def deletearticle(request, pk):
    article = Articles.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    context = {'article': article}
    return render(request, 'app/delete.html', context)
