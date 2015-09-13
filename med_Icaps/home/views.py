from django.shortcuts import render

# Create your views here.
 
def calendar(request):
    return render(request, 'home/index.html', {})


def index(request):
    return render_to_response('home/index.html')

