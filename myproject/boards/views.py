from django.http import HttpResponse


# Create your views here.
from boards.models import Board
from django.shortcuts import render


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})
