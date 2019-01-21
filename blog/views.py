from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils  import timezone
from .forms import PostForm
from .forms import SearchByStatForm
import requests

# Create your views here.

def home(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/home.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})    

def post_new(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
        	post = form.save(commit=False)
        	post.author = request.user
        	post.published_date = timezone.now()
        	post.save()
        	return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
		
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def tool(request):

    # load champion data
    url = 'http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json'
    response = requests.get(url)
    champion_data = response.json()
    champions = champion_data['data']


    # search champion by stat
    search_result={}    

    if request.method == "POST":
        #폼에 입력된 데이터를 view 페이지로 가지고 올 때
        form = SearchByStatForm(request.POST)
        if form.is_valid():
            search_result = form.search()

    else:    
       form = SearchByStatForm()


    return render(request, 'blog/tool.html',{
        #champion list
        'champions' : champions,
        #search list
        'form' : form, 'search_result' : search_result 

    })       
    # return render(request, 'blog/tool.html',{})    
