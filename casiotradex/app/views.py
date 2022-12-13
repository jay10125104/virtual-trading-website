from django.shortcuts import render,HttpResponse
from .models import Product,Option,SocialMedia
# Create your views here.
def login(request):
    return render(request,'app/index1.html')
def signup(request):
    return render(request,'app/index2.html');
def navbar(request):
    return render(request,'app/navbar.html');
def success(request):
    return render(request,'app/success.html');
def home(request):
    product = Product.objects.all()
    option = Option.objects.all()
    socialmedia = SocialMedia.objects.all()
    return render(request,'app/index.html',{'product':product,'option':option,'socialmedia':socialmedia})
def home2(request,data):
    print(data);
    if data!=None:
        product = Product.objects.all()
        return render(request,'app/index.html',{'product':product})