from django.shortcuts import render,redirect, get_object_or_404
from .models import Products, Article
from .form import FormulaireContactForm


def index(request):
    if request.method == "POST":
        form = FormulaireContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_shop:index')
    else:
        form = FormulaireContactForm()
    context = { 
        'produits': Products.objects.all(),
        'form': FormulaireContactForm()
    } 
    return render(request, 'doss_html/index.html', context)

def contact(request):
    if request.method == "POST":
        form = FormulaireContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_shop:index')
    else:
        form = FormulaireContactForm()
    return render(request, 'doss_html/index.html', {'form': form})
def article(request):
    articles = Article.objects.all()
    return render(request, 'doss_html/articles.html', {'articule': articles})



