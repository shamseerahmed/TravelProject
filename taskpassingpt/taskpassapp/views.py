from django.shortcuts import render

from . models import place
from . models import person

# Create your views here.
def demo(request):
    per = person.objects.all()

    obj =place.objects.all()


    return render(request,"index.html",{'result':obj,'result1':per})



