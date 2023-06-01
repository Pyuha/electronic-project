from django.shortcuts import render
from .models import ViewStuff

def main(request):

    return render(request, 'main.html')

def stuff(request):

    all_stuff = ViewStuff.objects.all()

    context = {
        'all_stuff' : all_stuff
    }

    return render(request, 'stuff.html', context)

def add_to_basket(request):

    if request.POST.get('add_to_basket') == 'Сохранить':

        ViewStuff.objects.create(
            promo    =request.POST.get('stuff_promo'),
            title    =request.POST.get('stuff_title'),
            price    =request.POST.get('stuff_price '),
        )

    return render(request, 'basket.html')

