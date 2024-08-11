from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_ = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all
    if sort_ == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_ == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_ == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
