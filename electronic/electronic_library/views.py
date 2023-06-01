from django.shortcuts import render
from .models import AddStuff

def main(request):

    return render(request, 'main.html')

def stuff(request):

    return render(request, 'stuff.html')

def add_to_basket(request):
    if request.POST.get('add_note') == 'Добавить':

        AddStuff.objects.create(
            title = request.POST.get('stuff_title'),
            type = request.POST.get('stuff_type'),
        )

    return render(request, 'basket.html')