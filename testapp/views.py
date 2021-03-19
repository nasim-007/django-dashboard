from django.shortcuts import render

from .models import helloWorld
# Create your views here.

def testview(request):
    mediatest = helloWorld.objects.all()

    context = {
        'mediatest': mediatest,
    }
    return render(request, "test.html", context)