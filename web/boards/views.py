from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board
# from redis import Redis

# Create your views here.

def home(request):
    boards = Board.objects.all()
    # boards_names = list()
    #
    # for board in boards:
    #     boards_names.append(board.name)
    #
    # resopse_html = '<br>'.join(boards_names)

    return render(request, 'home.html', {'boards':boards})


# redis = Redis(host='redis', port=6379)


# def home(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['item_text'])
#         return redirect('/')
#     items = Item.objects.all()
#     counter = redis.incr('counter')
#     return render(request, 'home.html', {'items': items, 'counter': counter})
