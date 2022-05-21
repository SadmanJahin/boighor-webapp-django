from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout
from django.contrib.auth.models import auth
from index.models import Footer

footerContent = Footer.objects.all()[0]

# Create your views here.
def login(request):
    verificationFailed=False
    data = {
        'verificationFailed': verificationFailed,
        'footer': footerContent,
    }
    if (request.method == 'POST'):
        phone = request.POST['phone']
        password = request.POST['password']
        User = get_user_model()
        user = authenticate(username=phone, password=password)
        if user is not None:
          auth.login(request,user)
          return redirect('user')
        else :
          data["verificationFailed"] = True
          return render(request, 'authentication/login.html',data)
    return render(request, 'authentication/login.html',data)


def registration(request):
    emailExist = False
    phoneExist = False
    data = {
        'emailExist': emailExist,
        'phoneExist': phoneExist,
        'footer': footerContent,
    }
    if (request.method == 'POST'):
        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        User=get_user_model()
        if User.objects.filter(phone=phone).exists():
            print("Phone Already Exists")
            data["phoneExist"] = True
        elif User.objects.filter(email=email).exists():
            print("Email already exists")
            data["emailExist"] = True
        else:
            USER=User.objects.create_user(phone=phone,username=name,password=password,email=email)
            USER.save()
            return  redirect('login')
    return render(request, 'authentication/registration.html',data)


def userlogout(request):
    logout(request)
    return redirect('login')
