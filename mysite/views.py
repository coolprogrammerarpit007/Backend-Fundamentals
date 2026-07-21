from django.http import HttpResponse



def index(Request):
    return HttpResponse("Hello World, you are on the Invoice Page. Nice to have you all!")