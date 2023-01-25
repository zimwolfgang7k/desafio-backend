from django.shortcuts import render
from django.http import HttpResponse
from .forms import Form


def home(request):
    formModel = Form()
    return render(request, "home.html", {"form": formModel})


def data_response(request):
    formResponse = Form(request.POST)
    codeData = formResponse.data["code"]
    return HttpResponse(codeData)
