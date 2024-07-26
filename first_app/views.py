from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')

def root(request):
    return render(request, 'root.html')

def hello(request):
    username = 'ehyong'

    context = {
        'username': username,
    }

    return render(request, 'hello.html', context)


def lunch(request):
    menus = ['볶음밥', '라면', '마라탕']

    pick = random.choice(menus)

    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):

    num = random.sample(range(1, 46), 6)

    context = {
        'num': num,
    }
    
    return render(request, 'lotto.html', context)