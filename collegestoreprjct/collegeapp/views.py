from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import django.contrib.messages
from django.contrib import auth, messages
from django.contrib.auth import authenticate,login


from.models import College_store,User_reg

from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def home(request):
  return render( request,'home.html')
def btn_click(request):
  return render(request,'login.html')
def reg(request):
    return render(request,'register.html')
def re_reg(request):

    return render(request,'studform.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    return render(request, 'newform.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('Password','')
        password_c = request.POST.get('Confirm_Password','')
        if password == password_c:
            if User_reg.objects.filter(username=username).exists():
                messages.info(request, "username is taken")
                return redirect('register')
            elif User_reg.objects.filter(password=password).exists():
                messages.info(request, "password is taken")
                return redirect('register')
            else:
                user = User_reg.objects.filter(username=username, password=password)
            user.save();
            return redirect("login.html")
        else:
            messages.info(request, "password not matched")
            return redirect('register.html')
    return redirect('/')


def form(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        age = request.POST.get('age','')
        dob = request.POST.get('dob','')
        gender = request.POST.get('gender','')
        phone = request.POST.get('phone','')
        mailid = request.POST.get('mailid','')
        address = request.POST.get('address','')
        dept = request.POST.get('dept', '')
        course = request.POST.get('course','')
        puropose = request.POST.get('purpose','')
        mat_provd = request.POST.get('mat_provd','')
        college= College_store( firstname=firstname,lastname=lastname, age=age, dob=dob, gender=gender, phone=phone,  mailid=mailid, address=address, dept=dept, course=course, puropose=puropose, mat_provd=mat_provd)
        college.save()
        return HttpResponse('Your order is placed')

    elif request.method=='GET':
       return render(request,'newform.html')
    else:
        return HttpResponse('an exception Occured')
def logout(request):
  auth.logout(request)
  return redirect('/')