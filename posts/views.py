from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Category ,Post, Comment
from .forms import AddPostForm, EditPostForm, AddCommentForm, AddReplyForm
from django.contrib import messages


def all_posts(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts ,
        'categories': categories,
    }
    return render(request, 'posts/all_posts.html', context)



def post_detail(request, year, month, day, post_id):
    post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day, id=post_id) 
    comments = Comment.objects.filter(post=post, is_reply=False)
    categories = Category.objects.all()
    reply_form = AddReplyForm()
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            cm = form.save(commit=False)
            cm.post = post
            cm.user = request.user
            cm.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
    form = AddCommentForm()
    context = {
        'post': post ,
        'comments': comments ,
        'form' : form,
        'reply_form': reply_form ,
        'categories': categories,
    }
    return render(request, 'posts/post_detail.html', context)



#@login_required
def user_dashboard(request, user_id):
    user = get_object_or_404(User, id = user_id)
    posts = Post.objects.filter(user = user)
    categories = Category.objects.all()
    context = {
        'user': user ,
        'posts': posts ,
        'categories': categories,
    }
    return render(request, 'posts/dashboard.html', context)


@login_required
def add_post(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'با موفقیت منتشر شد', 'success')
            return redirect('posts:dashboard', request.user.id)
    else :
        form = AddPostForm()
    context = {
        'form': form ,
        'categories': categories,
    }
    return render(request, 'posts/add_post.html', context)


@login_required
def delete_post(request, user_id ,post_id):
    if user_id == request.user.id :
        the_post = Post.objects.filter(id=post_id)
        the_post.delete()
        messages.success(request, 'با موفقیت حذف شد', 'success')
        return redirect('posts:dashboard', request.user.id)
    else :
        return redirect('posts:all_posts')


@login_required
def edit_post(request, user_id, post_id):
    categories = Category.objects.all()
    if user_id == request.user.id :
        the_post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = EditPostForm(request.POST, instance=the_post)
            if form.is_valid():
                form.save()
                messages.success(request, 'با موفقیت ویرایش شد', 'success')
                return redirect('posts:dashboard', request.user.id)
        else:
            form = EditPostForm(instance=the_post)
        context = {
            'form': form ,
            'categories': categories,
        }
        return render(request, 'posts/edit_post.html', context)
    else :
        return redirect('posts:all_posts')


@login_required
def add_reply(request, post_id, comment_id):
    the_post = get_object_or_404(Post, id = post_id)
    the_comment = get_object_or_404(Comment, id = comment_id)
    if request.method == 'POST':
        form = AddReplyForm(request.POST)
        if form.is_valid():
            rp = form.save(commit=False)
            rp.post = the_post
            rp.user = request.user
            rp.reply = the_comment
            rp.is_reply = True
            rp.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')
    return redirect('posts:post_detail', the_post.created.year, the_post.created.month, the_post.created.day, the_post.id)


def post_categories(request, cat_id):
    the_category = get_object_or_404(Category, id=cat_id)
    posts = Post.objects.filter(category=the_category)
    categories = Category.objects.all()
    context = {
        'posts':posts ,
        'categories': categories ,
        'the_category': the_category,
    }
    return render(request,'posts/post_categories.html',context)
