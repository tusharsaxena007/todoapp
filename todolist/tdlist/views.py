from django.shortcuts import render,HttpResponse,redirect,reverse
from .forms import list_input,loginform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .models import List
from datetime import datetime

@login_required(login_url='loginpage')
def homepage(request):
        user = request.user
        todolist = user.list_set.all()
        return render(request,'todolist/homepage.html',{'todolist':todolist})


class loginpage(View):

      def get(self,request):
         if request.user.is_authenticated:
             return redirect(reverse('homepage'))
         else:
             form = loginform()
             return render(request,'todolist/loginpage.html',{'form':form})


      def post(self,request):
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(username=username,password=password)
          if user is not None:
              login(request,user)
          else:
              return redirect(reverse('loginpage'))

          return redirect(reverse('homepage'))


def logout_view(request):
     logout(request)
     return redirect(reverse('homepage'))


class NewUser(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request,'todolist/newuser.html',{'form':form})


    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('loginpage'))
        else:
            return redirect(reverse('newuser'))


@login_required(login_url='loginpage')
def delete_view(request,pk):
    obj = List.objects.get(pk=pk)
    obj.delete()
    return redirect(reverse('homepage'))



class newtodo(View):

      def get(self,request):
          form  = list_input()
          return render(request,'todolist/newtodo.html',{'form':form})

      def post(self,request):
          if request.user.is_authenticated:
             form = list_input(request.POST)

             if form.is_valid():
                  td = List()
                  td.user = request.user
                  td.name = form.cleaned_data.get('name')
                  td.text = form.cleaned_data.get('text')
                  print(form.cleaned_data.get('flag'))
                  td.flag = form.cleaned_data.get('flag')
                  td.datetimemade = datetime.now()
                  print(datetime.now())
                  td.save()
                  return redirect(reverse('homepage'))
             else:
                return redirect(reverse('newtodo'))
          else:
              return redirect('loginpage')