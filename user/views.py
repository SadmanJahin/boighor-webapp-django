from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render
from django.template.backends import django
from django.utils.datetime_safe import datetime

from index.models import Footer
from book.models import Book
from .models import UserPost

profileActive="active"
footerContent = Footer.objects.all()[0]
context = {
'footer': footerContent,
'profileActive':profileActive,
}
# Create your views here.
def userBookPost(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        author = request.POST['author']
        price = request.POST['price']
        release_date = request.POST['release_date']
        category = request.POST['category']
        image = request.FILES['image']
        current_user = request.user
        if (name == "" or author == "" or price == "" or release_date == ""):
             checkEmpty = True
        else:
             checkEmpty = False
             bookData = Book()
             bookData.user_id =current_user.id
             bookData.bookName=name
             bookData.bookWriter = author
             bookData.price = price
             bookData.release_date = release_date
             bookData.bookCategory=category
             bookData.bookImage=image
             bookData.save()
             return render(request,'user/bookposts.html',context)
    else:
        return render(request,'user/bookposts.html',context)

def userProfile(request):
    if (request.method == 'POST'):
        post = request.POST['post']
        dateTime=datetime.now()
        postData=UserPost()
        postData.post=post
        postData.postDateTime=dateTime
        postData.save()

    postData = UserPost.objects.all()
    daysAgo=[]
    hourAgo = []
    for x in postData:
        now = datetime.now()
        naive = x.postDateTime.replace(tzinfo=None)
        days=abs(now-naive)
        min=int(days.seconds/60)
        hour=int(min/60)
        print(hour,min,days.seconds)
        daysAgo.append(days)
        hourAgo.append([hour,min])

    for x in hourAgo:
       print(x[0])
    # Person.Truncate(Person)
    # print(x.postDateTime.strftime('%b %d'))

    data = {
        'post_data': zip(postData, daysAgo,hourAgo),
        'footer': footerContent,
        'daysAgo': daysAgo,
        'profileActive': profileActive,
    }

    return render(request,'user/profile.html',data)