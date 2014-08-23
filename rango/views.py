from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hello world! <br/><a href='/rango/about'>Link to about page</a>")

def about(request):
    return HttpResponse("Here is the about page! <br/><a href='/rango/'>Link to home page</a>")
