from django.shortcuts import render
from .models import ViewStuff, AddStuff

def main(request):

    return render(request, 'main.html')

def stuff(request):

    all_stuff = ViewStuff.objects.all()

    context = {
        'all_stuff' : all_stuff
    }

    from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
    try:
        stuff = ViewStuff.objects.get(title=request.POST.get('stuff_title'))

        if len(AddStuff.objects.all()) > 0 and len(AddStuff.objects.filter(title=stuff.title)) > 0:
            print("Товар уже в списке")
        else:
            AddStuff.objects.create(
                title = stuff.title,
                price = stuff.price,
                promo = stuff.promo
            )
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        pass

    return render(request, 'stuff.html', context)

def basket(request):

    total_basket = 0
    basket = AddStuff.objects.all()

    return render(request, 'basket.html', {'basket' : basket, "total_basket":total_basket})

    

