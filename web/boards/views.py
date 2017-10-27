from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

from .models import Board, Topic, Post
from .forms import NewTopicForm
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


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    return render(request, 'topics.html', {'board':board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first() # TODO: get the currently logged in User

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            return redirect('board_topics', pk=board.pk) # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board':board, 'form':form})
