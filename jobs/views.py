from django.shortcuts import render
from .models import Jobs, Golf


# Create your views here.
def home(request):
    jobs = Jobs.objects
    return render(request, 'home.html', {'jobs':jobs})

def golf(request):
    golf = Golf.objects
    return render(request, 'golf.html', {'golf':golf})
