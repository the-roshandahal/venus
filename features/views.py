from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    context = {
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_obj = Contact.objects.create( name=name,email=email,contact=contact,subject=subject,message=message)
        contact_obj.save()
        return redirect('contact')
    else:

        context = {
        }
        return render(request,'contact.html',context)

def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request,'blogs.html',context)
    

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    recent_blogs = Blog.objects.all().exclude(slug=slug)
    print(recent_blogs)
    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blog_details.html', context)