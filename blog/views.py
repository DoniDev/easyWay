from django.shortcuts import render, get_object_or_404, redirect
from . models import Post
from .forms import PostForm, PostDeleteForm
from django.contrib.auth.decorators import permission_required
from taggit.models import Tag
from django.core.paginator import Paginator


def home(request, tag=None):
    tag_obj = None
    if not tag:
        posts = Post.objects.all()
    else:
        tag_obj = get_object_or_404(Tag, slug=tag)
        posts = Post.objects.filter(tags__in=[tag_obj])

    # here
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'section': 'home',
        'posts': posts,
        'tag': tag_obj,
        'page': page,
    }

    return render(request, 'blog/home.html', context=context)


def detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/detail.html', context=context)


@permission_required('blog:add_post', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:home')

    else:
        form = PostForm()

    context = {'form': form, 'section': 'blog_create'}
    return render(request, 'blog/create.html', context=context)


@permission_required('blog:change_post', raise_exception=True)
def edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'section': 'blog_edit',
        'post': post,
    }

    return render(request, 'blog/edit.html', context=context)

@permission_required('blog:delete_post', raise_exception=True)
def delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostDeleteForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            post.delete()
            return redirect('blog:home')

    else:
        form = PostDeleteForm(instance=post)

    context = {
        'form': form,
        'section': 'blog_delete',
        'post': post,
    }
    return render(request, 'blog/delete.html', context=context)

