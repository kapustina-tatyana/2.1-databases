from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()

    if 'sort' in request.GET:
        if request.GET['sort'] == 'name':
            all_phones = Phone.objects.all().order_by('name')
        elif request.GET['sort'] == 'max_price':
            all_phones = Phone.objects.all().order_by('-price')
        else:
            all_phones = Phone.objects.all().order_by('price')


    context = {'phones': all_phones,}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_info = Phone.objects.get(slug=slug)
    context = {'phone': phone_info}

    return render(request, template, context)
