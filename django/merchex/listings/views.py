from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request,
    'listings/hello.html',
    context = {'bands': bands})


def about(request):
    return HttpResponse("<h1>A propos</h1> <p>Nous adorons merch !</p>")

def contact(request):
    return HttpResponse("<h1>contact us.</h1>")

def listings(request):
    return HttpResponse("<h1>liste de listing</h1>")

# Create your views here.
