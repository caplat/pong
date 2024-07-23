from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
""")

def about(request):
    return HttpResponse("<h1>A propos</h1> <p>Nous adorons merch !</p>")

def contact(request):
    return HttpResponse("<h1>contact us.</h1>")

def listings(request):
    return HttpResponse("<h1>liste de listing</h1>")

# Create your views here.
