from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world you're at the polls index")
def testing(request):
    return HttpResponse("Hello welcome to testing")