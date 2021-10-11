from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def BlogView(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    blogg = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'posts': posts, 'blogg': blogg})


def BlogDetail(request, slug):
    post = Blog.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/index-detail.html', {'post': post, 'form': form})
