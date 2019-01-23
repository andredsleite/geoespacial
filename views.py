from django.shortcuts import render

# Create your views here.
def panda(request):
    return render(request,'panda.html');
