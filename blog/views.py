from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils  import timezone
from .forms import PostForm
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
    url = 'http://ddragon.leagueoflegends.com/cdn/8.13.1/data/en_US/champion.json'
    response = requests.get(url)
    champion_data = response.json()

    return render(request, 'blog/tool.html',{
        # 'champions': champion_data['data']

        # 'name' : champion_data['data']['Aatrox']['name'],
        # 'info' : champion_data['data']['Aatrox']['info'],

        'champion_data' : champion_data,

        'champions' : champion_data['data'],
    })       
    # return render(request, 'blog/tool.html',{})    

    