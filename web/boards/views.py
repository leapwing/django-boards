from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from redis import Redis

# Create your views here.

def hello(request):
    return HttpResponse("Hello, World!")


redis = Redis(host='redis', port=6379)


def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})
