from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import loginform,createuserform,profileform,blogform
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Blogpost
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect



def loginpage(request):
     if request.user.is_authenticated:
        return redirect(reverse('homepage'))
     else:
        form = loginform()
        return render(request,'homepage/loginform.html',{'form':form})



def logincheck(request):
     if request.POST:
          form = loginform(request.POST)
          print(form)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username,password=password)
               if user is not None:
                    login(request,user)
                    return redirect(reverse('homepage'))
               else:
                    return HttpResponse("not logged in")

          else:
               return HttpResponse("Form is not valid")

     else:
          return redirect(reverse('homepage'))


def logout_view(request):
     logout(request)
     return redirect(reverse('homepage'))


def createnewuser(request):
     if request.method=='GET':
          form = createuserform()
          return render(request,'homepage/createuserform.html',{'form':form})

     elif request.POST:
          form = createuserform(request.POST)
          if form.is_valid():
               print(form.user)
               user = User.objects.get(username=form.cleaned_data.get('username'))
               user.profile.bio = form.cleaned_data.get('bio')
               return HttpResponse("User Created")

          else:
               return HttpResponse("form is not valid ")




# THE MAIN APPLICATION FUNCTION BEGINS FROM HERE
#LET'S BEGIN


def homepage(request):
     if request.user.is_authenticated:
        user = request.user
        blogs = user.blogpost_set.all()
        return render(request,'homepage/homepage.html',{'blogs':blogs})
     else:
        return redirect(reverse('loginpage'))


def createnewblog(request):
     USER = request.user
     if request.method =='GET':
        form = blogform()
        return render(request,'homepage/createnewblog.html',{'form':form})

     elif request.POST:
          form = blogform(request.POST)
          if form.is_valid():
               b = Blogpost()
               b.user = USER
               b.text = form.cleaned_data.get('text')
               b.heading = form.cleaned_data.get('heading')
               b.subheading = form.cleaned_data.get('subheading')
               b.save()
          else:
               return HttpResponse("FORM not valid")

          return redirect(reverse('homepage'))

def deleteblog(request,pk):
     b = Blogpost.objects.get(pk=pk)
     b.delete()
     return redirect(reverse('homepage'))

def editblog(request,pk):
    if request.POST:
        form = blogform(request.POST)
        if form.is_valid():
            b = Blogpost()
            b.text = form.cleaned_data.get('text')
            b.heading = form.cleaned_data.get('heading')
            b.subheading = form.cleaned_data.get('subheading')
            b.category = form.cleaned_data.get('category')
            b.save()
        else:
            return HttpResponse("FORM not valid")


    elif request.method=='GET':
        blog = Blogpost.objects.filter(pk=pk).values()[0]
        form = blogform(initial=blog)
        return render(request,'homepage/editblog.html',{'form':form,'pk':pk})


def shareall(request):
     USER = request.user
     blogs = USER.blogpost_set.all()
     return render(request,'homepage/allposts.html',{'blogs':blogs})


def share(request,pk):
     blog = Blogpost.objects.get(pk=pk)
     url = str(request.path)
     url='http://127.0.0.1:8000'+url
     return render(request,'homepage/singlepost.html',{'blog':blog,'url':url})

@login_required(login_url='loginpage')
def likecount(request,pk):

    blog = Blogpost.objects.get(pk=pk)
    if blog.dislikes_count():
        blog.dislike.remove(request.user)
        blog.like.add(request.user)
        blog.save()
    else:
        blog.like.add(request.user)

    return HttpResponseRedirect(reverse('share',args=[int(pk)]))


@login_required(login_url='loginpage')
def dislikecount(request,pk):

    blog = Blogpost.objects.get(pk=pk)

    if blog.likes_count():
        blog.like.remove(request.user)
        blog.dislike.add(request.user)
        blog.save()
    else:
        blog.dislike.add(request.user)
    return HttpResponseRedirect(reverse('share',args=[int(pk)]))

