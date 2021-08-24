from django import forms
from django.db.models import manager
from django.http import request
from task.forms import *
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect,reverse
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm
from .models import MyUser,Manager,Skill
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model

user = get_user_model()


def index(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')


def emppage(request):
    return render(request,'emp.html')


def log(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            request.session['un'] = username
            return render(request,'home.html',{"user":user})
        else:
            return HttpResponse("INVALID CREDENTIALS")
    else:
        return render(request, 'login.html')

# def log(request):
#     if request.method=='POST':
#         if User.objects.filter(username=request.POST['Username'],password=request.POST['Password'],role=1).exists():
#                 x=User.objects.get(username=request.POST['Username'],password=request.POST['Password'],role=1)
#                 data=User.objects.all()
#                 username=request.POST['Username']
#                 request.session['Username']=username
#                 request.session['auth']=1
#                 return redirect('/home')
#         elif  User.objects.filter(username=request.POST['Username'],password=request.POST['Password'],role=2).exists():
#                 x=User.objects.get(username=request.POST['Username'],password=request.POST['Password'],role=2)
#                 return redirect('/emp')
#         else:
#             return HttpResponse("Invalid password and username")
#     else:
#         return render(request,'login.html')


def creemp(request):
    forms=UserCreationForm
    return render(request,'creemp.html',{'form':forms})


def ManagerSignup(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 1
            user.save()
            return render(request, 'login.html')
    else:
        form = RegForm
    return render(request, 'signup.html', {'form': form})


def EmployeeSignup(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.role = 2
            emp.save()
            request.session['un'] = emp.username
            return redirect('add skill')
    else:
        form = RegForm
    return render(request, 'signup.html', {'form': form})


def addskill(request):
    form = SkillForm
    labels = []
    data = []
    pk = request.session['un']
    skills = Skill.objects.filter(pk=pk).all()
    for s in skills:
        labels.append(s.Sname)
        data.append(s.percentage)
    return render(request, 'add_skill.html', {'form': form, 'labels': labels, 'data': data})



def manageEmployees(request):
    emp_list = MyUser.objects.filter(role=2)
    return render(request, 'emp_list.html',{'list':emp_list})


def profileview(request):
    user = request.user
    return render(request, 'emp_profile.html')


def load_skills(request):
    un = request.session['un']
    user = MyUser.objects.get(pk=un)
    skills = Skill.objects.filter(ref=user)
    return render(request, 'skills.html', {'skills': skills})


def add_skill(request):
    if request.method=="GET":
        sname = request.GET.get('sname')
        sp = request.GET.get('sp')
        un = request.session['un']
        u = MyUser.objects.get(pk=un)
        s = Skill(Sname=sname, percentage=sp, ref=u)
        s.save()
        return redirect('load skill')


def edit_skill(request, pk):
    request.session['sid'] = pk
    if request.method == "POST":
        s = request.POST.get('skill')
        p = request.POST.get('percentage')
        p_k = request.session['sid']
        Skill.objects.filter(pk=p_k).update(Sname=s, percentage=p)
        return redirect('add skill')
    else:
        s=Skill.objects.get(pk=pk)
        return render(request, 'edit_skill.html', {'skill':s})


def delete_skill(request, pk):
    Skill.objects.get(pk=pk).delete()
    return redirect('add skill')


def delete_employee(request, pk):
    MyUser.objects.get(pk=pk).delete()
    return redirect('manage employees')


def userlogout(request):
    logout(request)
    return redirect('login')


def manageSkill(request, pk):
    request.session['un'] = pk
    return redirect('add skill')