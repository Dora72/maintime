
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    context = {
        "datetime": now,
    }
    return render(request, 'index.html', context)

# Create your views here.
