from multiprocessing import context
from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

rooms= [
    {'id':1,'name':'Learning Python'},
    {'id':2,'name':'Design'},
    {'id':3,'name':'frontend dev'},

]

def home(request):
    context={'rooms':rooms}
    
    return render(request, 'home.html',context)
def room(request): 
    return render(request, 'room.html')
#def index(request):
    #return HttpResponse('lol')
    