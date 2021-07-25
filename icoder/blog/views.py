from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.

def bloghome(request):
    # print('aksh12', request)
    allposts = Post.objects.all()
    a = [i for i in range(0, 1000)]
    import random
    b = random.randint(1, 100)
    context = {'allposts1':allposts, 'b':b}
    # print(context)
    # for i in context['allposts1']:
    #     print(i)
    return render(request, 'blog/bloghome1.html', context)

    # return HttpResponse('<h1>This is a home1.<h1>')


def blogpost(request, myid1):
    myposts = Post.objects.filter(sno=myid1)[0]
    myposts.views += 1
    myposts.save()
    comments1 = BlogComment.objects.filter(post=myposts, parent=None)
    replies = BlogComment.objects.filter(post=myposts).exclude(parent=None)
    repDict = {}
    a = comments1.union(replies)
    a1 = len(a)
    print('comments1', replies)
    for item11 in replies:
        if item11.parent.sno not in repDict.keys():
            repDict[item11.parent.sno] = [item11]
        else:
            repDict[item11.parent.sno].append(item11)

    print('repdict', repDict)

    params = {'myposts' : myposts, 'comments1':comments1, 'user99':request.user, 'repDict':repDict, 'a1':a1}
    return render(request, 'blog/blogpost1.html', params)
    # return HttpResponse(f'<h1>This is a blog</h1>{slug}')


def postcomment(request):
    if request.method == 'POST':
        comment1 = request.POST.get('comment')
        user1 = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.filter(sno=postSno)[0]
        parentsno =  request.POST.get('parentsno')
        if parentsno == "":
            comment = BlogComment(comment1=comment1, user=user1, post=post)
            messages.success(request, 'your comment has been posted succesfuly')
            comment.save()
        else:
            parent = BlogComment.objects.filter(sno=parentsno)[0]
            comment = BlogComment(comment1=comment1, user=user1, post=post, parent = parent)
            messages.success(request, 'your reply has been posted succesfuly')
            comment.save()




        # print('comment1 = ', comment1, 'user = ', user1, 'postSno = ' ,postSno, ' post = ',post)
    #
    return redirect(f'/blog/contin/{postSno}/')

