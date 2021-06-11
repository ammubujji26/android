from django.shortcuts import render,redirect
from productsapp.forms import ProductsForm
from productsapp.models import Products


# Create your views here.
def create_view(request):
    print("create view",1)
    form=ProductsForm()
    if request.method=="POST":
        print("create view",)
        form=ProductsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/display')
    return render(request,'productsapp/create.html',{'form':form})
def display_view(request):
    form=Products.objects.all()
    print("forms data",form)
    return render(request,'productsapp/display.html',{'forms':form})

def update_view(request,id):
    products=Products.objects.get(id=id)
    if request.method=="POST":
        form=ProductsForm(request.POST,instance=products)
        form.save()
        return redirect('/display')
    return render(request,'productsapp/update.html',{'form':products})
def delete_view(request,id):
    products=Products.objects.get(id=id)
    products.delete()
    return redirect('/display')
