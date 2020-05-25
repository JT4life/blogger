from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment, AddComment
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
from blog.forms import CommentForm

def index(request):
    all_post = Post.objects.all()
    order_name = Post.objects.order_by("title")
    #paginator = Paginator(all_post, 3)
    #page = request.GET.get('page')
    #all_post = paginator.get_page(page)
    return render(request, "blogReview/index.html", {'Blogs': all_post}, {'Order': order_name})



def add_comment(request):
    t = request.GET.get('comment', 'default')
    b_id = request.GET.get('b_id', 'default')
    x1 = Post.title = b_id
    x = AddComment(text=t, post=x1)
    x.save()
    return HttpResponseRedirect(reverse('index'))


def add_comment_submit(request):
    print("Comment has been added")
    c = request.POST.get('comment', 'default')
    user = request.POST.get('username', 'default')
    info = AddComment(text=c, user=user)
    info.save()

    return render(request, "blogReview/header.html")


def login(request):
    return render(request, "blogReview/login.html")

def addBlog(request):
    return render(request, "blogReview/add_blog.html")

def add_blog_form_submit(request):
    print("Form has been submitted!")
    title = request.POST.get("title")
    body = request.POST.get("body")
    slug = request.POST.get("slug")
    guest = request.POST.get("author")
    #author = request.POST["author"]
    publish = request.POST.get("datepublish")
    #created = request.POST[""]
    #updated = request.POST[""]
    website = request.POST.get("website")

    blog_info = Post(title=title, body=body, slug=slug, publish=publish, website=website)

    blog_info.save()
    return render(request, "blogReview/index.html")

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blogReview/register.html', {'form':form})

@login_required
def dashboardView(request):
    return render(request, 'blogReview/dashboard.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'blogReview/index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogReview/post_detail.html'

