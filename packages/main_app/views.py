from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.http import Http404
from .models import Post, Category, UserExtended, UserPostRelation
from .utils import *
from django.http import JsonResponse



def index(request):
    posts = Post.objects.order_by('-publish_date').filter(status="p")  # showing only published posts
    
    post_per_page = get_post_per_page(request)
    
    p = Paginator(posts, post_per_page)
    total_pages = p.num_pages  # or last page
    
    # pagination
    if request.GET.get('page'):
        try:
            page = int(request.GET.get('page'))
        except:
            page = 1
    
    # if direct homepage
    else:
        page = 1
    
    try:
        latest_posts = p.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        latest_posts = p.page(total_pages)
        page = total_pages
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        latest_posts = p.page(1)
        page = 1
    
    if request.user.is_authenticated():
        """
        if logged in user
        liked post will be marked in homepage
        """
        user = UserExtended.objects.get(user=request.user)
        for p in latest_posts:
            try:
                p.have_like = "1" if UserPostRelation.objects.get(user=user, post=p) else "0"
            except:
                p.have_like = "0"
    
    pg_iter = long_pagination(
        current_page=page,
        total_pages=total_pages,
        showing=get_page_number_in_pagination(request),    # page number showing in pagination
        is_not_mobile=not request.is_mobile
    )

    popular_posts = Post.objects.order_by('-likes')[:5]
    all_cats = Category.objects.filter(post__likes__isnull=False).annotate(like_count=Sum('post__likes')).order_by(
        '-like_count')
    
    ctx = {  # context
        "posts": latest_posts,
        "popular_posts": popular_posts,
        "popular_cats": all_cats[:5],
        "all_cats": all_cats,
        "page_iter": pg_iter,
        "current_page": page,
    }
    return render(request, 'main_app/index.html', ctx)


def each_post(request, slug, pk):
    share_urls = {}
    post = get_object_or_404(Post, id=pk)
    if post.status != 'p':
        raise Http404("আপনার এহেন বোকামির জন্য আমরা শোক প্রকাশ করছি।কারণ, এই নামের কিছুই খুঁজে পাওয়া যায় নি!")

    if request.user.is_authenticated:
        user = UserExtended.objects.get(user=request.user)
        #liking_post(user, post, UserPostRelation)  # forcefully liking when visiting page
        
        try:    # if logged in user liked post will be marked
            post.have_like = "1" if UserPostRelation.objects.get(user=user, post=post) else "0"
        except:
            post.have_like = "0"
    
    full_url = str(request.scheme) + "://" + str(request.get_host()) + str(post.get_absolute_url())
    
    share_urls["fb"] = "https://www.facebook.com/plugins/share_button.php?href=" + \
                       full_url + \
                       "&layout=button_count&size=small&mobile_iframe=true&width=70&height=30&appId"
    share_urls["twt"] = "http://twitter.com/share?text=visit www.9moja.com for more&url=" + \
                        full_url + "&hashtags=মজা,নয়মজা,ফানি,9moja,funny,meme,bangla_meme"
    share_urls["gp"] = "https://plus.google.com/share?url=" + full_url
    
    from_page = request.GET.get('from_page') if request.method == 'GET' else 1
    
    popular_posts = Post.objects.order_by('-likes')[:5]
    popular_cats = Category.objects.filter(post__likes__isnull=False).annotate(like_count=Sum('post__likes')).order_by(
        '-like_count')[:5]
    
    ctx = {  # context
        'post': post,
        "popular_posts": popular_posts,
        "popular_cats": popular_cats,
        'from_page': from_page,
        'media_url': post.img.url,
        'share_urls': share_urls,
    }
    return render(request, 'main_app/single_post.html', ctx)


def each_category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        
        posts_by_category = Post.objects.filter(categorize__category=category).order_by('-publish_date')
        
        post_per_page = get_post_per_page(request)
        
        p = Paginator(posts_by_category, post_per_page)
        total_pages = p.num_pages  # or last page

        # pagination
        if request.GET.get('page'):
            try:
                page = int(request.GET.get('page'))
            except:
                page = 1

        # if direct homepage
        else:
            page = 1

        try:
            categorized_post = p.page(page)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            categorized_post = p.page(total_pages)
            page = total_pages
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            categorized_post = p.page(1)
            page = 1

        if request.user.is_authenticated():
            """
            if logged in user
            liked post will be marked in homepage
            """
            user = UserExtended.objects.get(user=request.user)
            for p in categorized_post:
                try:
                    p.have_like = "1" if UserPostRelation.objects.get(user=user, post=p) else "0"
                except:
                    p.have_like = "0"

        pg_iter = long_pagination(
            current_page=page,
            total_pages=total_pages,
            showing=get_page_number_in_pagination(request),  # page number showing in pagination
            is_not_mobile=not request.is_mobile
        )
    
    except Category.DoesNotExist:
        raise Http404("আপনার এহেন বোকামির জন্য আমরা শোক প্রকাশ করছি।কারণ, এই নামের কিছুই খুঁজে পাওয়া যায় নি!")

    popular_posts = Post.objects.order_by('-likes')[:5]
    popular_cats = Category.objects.filter(post__likes__isnull=False).annotate(like_count=Sum('post__likes')).order_by(
        '-like_count')[:5]
    
    ctx = {
        "is_category_template": True,
        "posts": categorized_post,
        "popular_posts": popular_posts,
        "popular_cats": popular_cats,
        "page_iter": pg_iter,
        "current_page": page,
    }
    return render(request, 'main_app/index.html', ctx)


def coming_soon(request):
    return render(request, 'main_app/coming-soon.html')


def search(request):
    result = None
    err = None
    if request.method == 'GET':
        keyword = request.GET.get('q')  # search keyword
        
        if keyword:
            posts = Post.objects.filter(title__contains=keyword)  # post
            cats = Category.objects.filter(name__contains=keyword)  # categories
            result = {
                "posts": posts,
                "cats": cats
            }
            err = None if posts or cats else "No result"
        else:
            # if no search keyword found, redirect to homepage
            return redirect('/')
    
    ctx = {
        "result": result,
        "err": err
    }
    return render(request, 'main_app/search.html', ctx)


def like_post(request):
    if request.method == 'GET':
        ajax_data = request.GET
        pk = ajax_data.get("post_id")
        jd = {}
        
        post = Post.objects.get(id=pk)
        user = UserExtended.objects.get(user=request.user)

        # initially no disliking !!! :D :D
        #if ajax_data.get("is_liked") == "1":
            # dislike
            # liking_post(user, post, UserPostRelation, False)
            # jd["is_liked"] = "0"
        if ajax_data.get("is_liked") == "0":
            # like
            liking_post(user, post, UserPostRelation)
            jd["is_liked"] = "1"
        else:
            # empty response
            # old value won't change
            jd["is_liked"] = ajax_data.get("is_liked")
            return JsonResponse(jd)
        
        # jd["likes"] = post.likes
        
        # print(jd)
        
        return JsonResponse(jd)
    
    return JsonResponse({
        "error": {
            "message": "Unexpected Error"
        }
    })


def popular_categories(request):
    popular_cat = Category.objects.filter(post__likes__isnull=False).annotate(like_count=Sum('post__likes')).order_by(
        '-like_count')[0]
    return each_category(request, popular_cat.slug)


def best_meme(request):
    popular_posts = Post.objects.order_by('-likes')[0]
    return each_post(request, popular_posts.slug, popular_posts.id)


def terms(request):
    return render(request, 'main_app/terms.html')