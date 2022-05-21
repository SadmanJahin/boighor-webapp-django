from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datetime_safe import datetime

from user.models import UserPost
from .models import Person
from .models import Footer

homeActive="active"
footerContent = Footer.objects.all()[0]
context = {
    'footer': footerContent,
'homeActive':homeActive,
}

# Create your views here.

def home(request):
    return render(request,'index/index.html',context)

def test(request):
    return HttpResponse("Hi Test")

def login(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        messege=request.POST['messege']
        
        
    if(name=="" or  email=="" or  phone=="" or messege==""):
        checkEmpty=True
    else:
        checkEmpty = False
        personData=Person()
        personData.name=name
        personData.email=email
        personData.phone=phone
        personData.messege=messege
        personData.save()
    
    
    personList=Person.objects.all()
            
    #Person.Truncate(Person)
    
    
    data={
        'person':personList,
        'checkEmpty':checkEmpty
    }
    
        
        
    return render(request,'index/welcome.html',data)

def helpPost(request):
    postData = UserPost.objects.all()
    daysAgo = []
    hourAgo = []
    for x in postData:
        now = datetime.now()
        naive = x.postDateTime.replace(tzinfo=None)
        days = abs(now - naive)
        min = int(days.seconds / 60)
        hour = int(min / 60)
        print(hour, min, days.seconds)
        daysAgo.append(days)
        hourAgo.append([hour, min])

    for x in hourAgo:
        print(x[0])
    # Person.Truncate(Person)
    # print(x.postDateTime.strftime('%b %d'))

    data = {
        'post_data': zip(postData, daysAgo, hourAgo),
        'footer': footerContent,
        'daysAgo': daysAgo,
    }

    return render(request, 'index/help-posts.html', data)