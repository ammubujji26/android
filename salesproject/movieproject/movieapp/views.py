from django.shortcuts import render
from movieapp.forms import Movie
from movieapp import models


# Create your views here.
def movie_view(request):
    return render(request,'movieapp/index.html')
def add_movie(request):
    print("Method name",request.method)
    form=Movie()
    if request.method=="POST":
        print("inside if")
        form=Movie(request.POST)
        print("after form")
        if form.is_valid():
            print("valid or not")
            form.save()
        return movie_view(request)
    return render(request,'movieapp/addmovie.html',{'form':form})
def list_movie(request):
    form=models.MovieForm.objects.all().order_by('-rating')
    return render(request,'movieapp/listmovie.html',{'list_movie':form})


def count_view(request):
    print("AMMU",request.COOKIES)
    if 'count' in request.COOKIES:
        print("hello",request.COOKIES)
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'movieapp/product.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response
