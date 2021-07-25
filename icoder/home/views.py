from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    print('aksh12', request)
    context = Post.objects.all()
    print('context', context)
    list1 = []
    list2 = []
    for i in context:
        v = i.views
        list1.append(v)
    list1.sort()
    print('list1', list1)
    s = list1[len(list1)-3:]
    s.reverse()
    print('s',s)
    for i in context:
        if i.views in s:
            list2.append(i)
    print('list2', list2)
    print('popat', context)
    context1 = {'a':list2}

    # return HttpResponse('<h1>This is a home.<h1>')
    return render(request, 'home/home1.html' ,context1)

def contact(request):
    # messages.success(request, 'Profile details updated.')
    # messages.error(request, 'Profile details updated.')
    # messages.info(request, 'Profile details updated.')
    if request.method == 'POST':
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        phone = request.POST.get('phone1')
        content = request.POST.get('content')

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please Enter your name')
        else:
            messages.success(request, 'Your form has been successfully sent.')
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
    return render(request, 'home/contact.html')
    # return HttpResponse('<h1>This is a contact</h1>')

def search(request):
    query = request.GET.get('search1')
    print('query', query)
    allpoststitle = Post.objects.filter(title__icontains=query)
    allpostscontent = Post.objects.filter(content__icontains=query)
    allposts100 = allpoststitle.union(allpostscontent)
    if len(allposts100) == 0:
        messages.warning(request, 'Your Search query is did not match any our products. please Enter a valid query')
    else:
        messages.success(request, f'This is your {query} results. Enjoy it....')
    print('allposts100', allposts100)
    params = {'allposts100':allposts100, 'query':query}
    return render(request, 'home/search.html', params)
    # return HttpResponse('This is Search')


def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse('<h1>This is a about</h1>')

def handlesignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(name) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('home')

        myuser = User.objects.create_user(name, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your iCoder account has been successfully created')
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')

def handlelogin(request):
    if request.method == 'POST':
        loginname = request.POST['loginname']
        loginpass1 = request.POST['loginpass1']

        user = authenticate(username=loginname, password=loginpass1)

        if user is not None:
            print('user9',user)
            login(request, user)
            messages.success(request, 'successfully logged in')
            param = {'user1':user}
            return render(request, 'home/home1.html', param)
            # return redirect('home')

        else:
            messages.error(request, 'Invalid creditials; please try again')
            return redirect('home')

    else:
        return HttpResponse('404 - Not found')

def handlelogout(request):
     logout(request)
     messages.success(request, 'Successfully logged out')
     param = {'user1':''}
     return render(request, 'home/home1.html', param)



