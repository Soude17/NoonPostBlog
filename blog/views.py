from django.shortcuts import render,get_object_or_404
from .models import Article,Category


def article_detail(request,slug):
    latest_articles = Article.objects.filter(status=True).order_by('-created')[:4]
    categories = Category.objects.all()
    article = get_object_or_404(Article,slug=slug)
    viewed_articles = request.session.get('viewed_articles', [])
    if article.id not in viewed_articles:
        article.views += 1
        article.save(update_fields=['views'])
        viewed_articles.append(article.id)
        request.session['viewed_articles'] = viewed_articles
    context ={
        'article':article,
        'latest_articles':latest_articles,
        'categories':categories,
    }
    return render(request,'blog/article_detail.html',context)


def article_list(request):
    latest_articles = Article.objects.filter(status=True).order_by('-created')[:4]
    categories = Category.objects.all()
    articles = Article.objects.filter(status=True)
    context ={
        'articles':articles,
        'latest_articles':latest_articles,
        'categories':categories,
    }
    return render(request,'blog/article_list.html',context)    

def category_article(request,slug):
    latest_articles = Article.objects.filter(status=True).order_by('-created')[:4]
    categories = Category.objects.all()
    category = get_object_or_404(Category,slug=slug)
    articles = Article.objects.filter(status=True,category=category)
    context ={
        'category':category,
        'articles':articles,
        'latest_articles':latest_articles,
        'categories':categories,
    }
    return render(request,'blog/category_article.html',context)
    